from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app import models


class AuthRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, first_name: str, last_name: str, email: str, password_hash: str) -> models.User:
        user = models.User(first_name=first_name, last_name=last_name, email=email.lower(), password_hash=password_hash)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> models.User | None:
        return self.db.query(models.User).filter(models.User.email == email.lower()).first()

    def get_user_by_id(self, user_id: int) -> models.User | None:
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def save_refresh_token(self, user_id: int, token_hash: str, expires_at: datetime) -> None:
        entry = models.RefreshToken(user_id=user_id, token_hash=token_hash, expires_at=expires_at)
        self.db.add(entry)
        self.db.commit()

    def get_active_refresh_token(self, token_hash: str) -> models.RefreshToken | None:
        now = datetime.now(timezone.utc)
        return (
            self.db.query(models.RefreshToken)
            .filter(
                models.RefreshToken.token_hash == token_hash,
                models.RefreshToken.revoked.is_(False),
                models.RefreshToken.expires_at > now,
            )
            .first()
        )

    def revoke_refresh_token(self, token_id: int) -> None:
        token = self.db.query(models.RefreshToken).filter(models.RefreshToken.id == token_id).first()
        if token:
            token.revoked = True
            self.db.commit()

    def ensure_base_roles(self) -> None:
        for role_name in ["admin", "doctor", "patient"]:
            role = self.db.query(models.Role).filter(models.Role.name == role_name).first()
            if not role:
                self.db.add(models.Role(name=role_name, description=f"Default role: {role_name}"))
        self.db.commit()
        permission = self.db.query(models.Permission).filter(models.Permission.name == "manage_users").first()
        if not permission:
            permission = models.Permission(name="manage_users", description="Can view all users.")
            self.db.add(permission)
            self.db.commit()
            self.db.refresh(permission)
        admin_role = self.db.query(models.Role).filter(models.Role.name == "admin").first()
        if admin_role:
            exists = (
                self.db.query(models.RolePermission)
                .filter(
                    models.RolePermission.role_id == admin_role.id,
                    models.RolePermission.permission_id == permission.id,
                )
                .first()
            )
            if not exists:
                self.db.add(models.RolePermission(role_id=admin_role.id, permission_id=permission.id))
                self.db.commit()

    def assign_role_if_absent(self, user_id: int, role_name: str) -> None:
        role = self.db.query(models.Role).filter(models.Role.name == role_name).first()
        if not role:
            return
        existing = (
            self.db.query(models.UserRole)
            .filter(models.UserRole.user_id == user_id, models.UserRole.role_id == role.id)
            .first()
        )
        if not existing:
            self.db.add(models.UserRole(user_id=user_id, role_id=role.id))
            self.db.commit()

    def get_user_permissions(self, user_id: int) -> set[str]:
        permissions = (
            self.db.query(models.Permission.name)
            .join(models.RolePermission, models.RolePermission.permission_id == models.Permission.id)
            .join(models.UserRole, models.UserRole.role_id == models.RolePermission.role_id)
            .filter(models.UserRole.user_id == user_id)
            .all()
        )
        return {perm[0] for perm in permissions}

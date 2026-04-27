from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.Services.auth_service import AuthService


def get_current_user(
    db: Session = Depends(get_db),
    authorization: str | None = Header(default=None, convert_underscores=False),
):
    if not authorization or not authorization.lower().startswith("bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing bearer token.")
    token = authorization.split(" ", 1)[1]
    return AuthService(db).get_current_user_from_token(token)


def require_permissions(required_permissions: list[str]):
    def dependency(
        user=Depends(get_current_user),
        db: Session = Depends(get_db),
    ):
        AuthService(db).check_permissions(user.id, required_permissions)
        return user

    return dependency

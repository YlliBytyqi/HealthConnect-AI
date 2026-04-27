from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.database import get_db
from app.deps import get_current_user, require_permissions
from app.schemas import LoginInput, RefreshInput, TokenResponse, UserCreate, UserRead
from app.Services.auth_service import AuthService

router = APIRouter(prefix="/api/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    return AuthService(db).register(payload.first_name, payload.last_name, payload.email, payload.password)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginInput, db: Session = Depends(get_db)):
    return AuthService(db).login(payload.email, payload.password)


@router.post("/refresh", response_model=TokenResponse)
def refresh(payload: RefreshInput, db: Session = Depends(get_db)):
    return AuthService(db).refresh(payload.refresh_token)


@router.get("/me", response_model=UserRead)
def me(user=Depends(get_current_user)):
    return user


@router.get("/admin/users")
def list_users_for_admin(
    _: object = Depends(require_permissions(["manage_users"])),
    db: Session = Depends(get_db),
):
    return [{"id": u.id, "email": u.email, "is_active": u.is_active} for u in db.query(models.User).all()]

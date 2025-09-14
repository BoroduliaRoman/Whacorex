from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_user_service
from app.core.jwt import create_access_token
from app.schemas.user import Token, UserCreate, UserLogin, UserOut
from app.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate, svc: UserService = Depends(get_user_service)):
    try:
        user = svc.register(payload)
    except ValueError as e:
        # email conflict - 409
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e)) from e
    return user


@router.post("/login", response_model=Token)
def login(payload: UserLogin, svc: UserService = Depends(get_user_service)):
    user = svc.authenticate(payload.email, payload.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials"
        )
    token = create_access_token(sub=user.id)
    return {"access_token": token, "token_type": "bearer"}

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_user_service
from app.schemas.user import UserCreate, UserOut
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

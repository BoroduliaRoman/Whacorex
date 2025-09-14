from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.db.models.user import User
from app.repositories.user import create_user, get_user_by_email
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def register(self, data: UserCreate) -> User:
        # 1) проверим дубликат
        if get_user_by_email(self.db, data.email):
            raise ValueError("user with this email already exists")

        # 2) захешируем пароль
        hashed = get_password_hash(data.password)

        # 3) создаём
        try:
            user = create_user(self.db, email=data.email, hashed_password=hashed)
        except IntegrityError:
            # на случай гонки/уникального индекса
            raise ValueError("user with this email already exists")

        return user

    def authenticate(self, email: str, password: str) -> User | None:
        user = get_user_by_email(self.db, email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

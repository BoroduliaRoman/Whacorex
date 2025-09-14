from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.models.user import User


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.scalar(select(User).where(User.email == email))


def create_user(db: Session, email: str, hashed_password: str) -> User:
    obj = User(email=email, hashed_password=hashed_password)
    db.add(obj)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        # пробрасываем наверх — выше решим, какой ответ отдать
        raise
    db.refresh(obj)
    return obj

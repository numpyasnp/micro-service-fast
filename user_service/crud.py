from .schemas import UserCreate
from sqlalchemy.orm import Session
from . import auth
from .models import User


def create_user(db: Session, user: UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    user = User(
        name=user.name,
        email=user.email,
        age=user.age,
        hashed_password=hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

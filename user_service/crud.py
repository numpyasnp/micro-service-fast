from pydantic import EmailStr

from .schemas import UserCreate
from sqlalchemy.orm import Session
from . import auth
from app.user_service import crud
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


def get_user(db: Session, pk: int):
    return db.query(User).filter(User.id == pk).first() # type: ignore

def get_user_by_email(db: Session, email: EmailStr):
    return db.query(User).filter(User.email == email).first() # type: ignore

def authenticate_user(db: Session, email: EmailStr, password: str):
    user = crud.get_user_by_email(db=db, email=email)
    if not user or not auth.verify_password(password, user.hashed_password):
        return None
    return user

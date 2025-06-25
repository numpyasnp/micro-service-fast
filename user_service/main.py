from app.user_service.schemas import User, UserCreate
from app.user_service import crud
from app.user_service.models import Base
from app.user_service.auth import get_db
from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session

from app.user_service.database import engine
from app.user_service.schemas import UserLogin

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Service",
    description="Microservice for user management",
    version="1.0.0"
)

@app.post("/users/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User already exists"
        )
    new_user = crud.create_user(db=db, user=user)
    return new_user

@app.get("/users/{pk}", response_model=User, status_code=status.HTTP_200_OK)
def get_user(pk: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, pk)
    return user

@app.post("/users/login", status_code=status.HTTP_200_OK)
def login(user_credential: UserLogin, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db=db, email=user_credential.email, password=user_credential.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong credential",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # todo: generate jwt token

    return {"token": f"test_jwt{user.id}", "token_type": "bearer"}

from app.user_service.schemas import User, UserCreate
from app.user_service.crud import create_user
from app.user_service.models import Base
from app.user_service.auth import get_db
from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session

from app.user_service.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Service",
    description="Microservice for user management",
    version="1.0.0"
)

@app.post("/users/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    return new_user

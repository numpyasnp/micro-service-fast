# bu dosya main fast api yi içerecek

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel
from .models import Order

app = FastAPI()

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

async_engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

SQLModel.metadata.create_all(async_engine)
@app.get("/")
def home():
    return {"message": "order-service-root"}

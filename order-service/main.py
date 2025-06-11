from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel

from .models import Order

app = FastAPI()

DATABASE_URL = "postgresql+asyncpg://ugurcan:postgre@localhost:5432/order_service"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

async def get_session():
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
def home():
    return {"message": "order-service-root"}

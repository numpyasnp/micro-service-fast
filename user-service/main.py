# bu dosya main fast api yi içerecek

from fastapi import FastAPI
from sqlmodel import create_engine, SQLModel
from .models import User

app = FastAPI()

sqlite_file_name = "user-service.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

SQLModel.metadata.create_all(engine)


@app.get("/")
def home():
    return {"message": "user-service-root"}

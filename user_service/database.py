import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base, Session

DATABASE_URL = "postgresql://ugurcan:postgre@localhost:5432/user_service"

engine = create_engine(os.getenv("DATABASE_URL", DATABASE_URL))

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

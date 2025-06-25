from sqlalchemy import Column, Integer, Boolean, DateTime, String
from .database import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__="users"

    id=Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    age = Column(Integer, nullable=True, default=None)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


"""
user_id int ile order modeline bağlan

order_create edildiğinde bir event yayinla. bu event içinde user_id'de olsun.
bunun için rabbitmq (message broker -> producer'dan alip consumera iletecek kisim) gerekiyor.

yani order-producer ilk etapta gerekli.

"""

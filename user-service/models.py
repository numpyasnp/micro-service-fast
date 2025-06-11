from typing import Optional

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: Optional[str] = Field(unique=True, index=True) # need email field validation
    age: Optional[int] = Field(default=None)

"""
user_id int ile order modeline bağlan

order_create edildiğinde bir event yayinla. bu event içinde user_id'de olsun.
bunun için rabbitmq (message broker -> producer'dan alip consumera iletecek kisim) gerekiyor.

yani order-producer ilk etapta gerekli.

"""

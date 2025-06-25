from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    name: str
    age: Optional[int] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: str
    age: Optional[int] = None


class User(UserBase):
    id: int
    is_active: bool

class UserLogin(BaseModel):
    email: EmailStr
    password: str

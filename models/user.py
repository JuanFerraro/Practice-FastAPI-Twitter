# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# User Model:
class UserBase(BaseModel):
    user_id: UUID = Field()
    email: EmailStr = Field()

class UserLogin(UserBase):
    password: str = Field(min_length=8)

class User(UserBase):
    first_name: str = Field(min_length=1, max_length=30)
    last_name: str = Field(min_length=1, max_length=30)
    birth_date: Optional[date] = Field(None)


# Tweet Model:
class Tweet(BaseModel):
    pass
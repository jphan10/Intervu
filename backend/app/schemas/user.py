# Pydantic Model for input/output of API
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str # Plain text password, needs to be hashed

class UserResponse(UserBase):
    id: int
    role: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
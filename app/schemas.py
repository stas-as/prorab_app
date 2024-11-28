from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    password: str
    group: Optional[str] = "user"

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime
    group: str

    class Config:
        orm_mode = True

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str
    category: str
    responsible_user_id: int
    author_user_id: int

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    category: str
    responsible_user_id: int
    author_user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    text: str
    author_user_id: int

class CommentResponse(BaseModel):
    id: int
    text: str
    author_user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CategoryCreate(BaseModel):
    name: str
    description: str

class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
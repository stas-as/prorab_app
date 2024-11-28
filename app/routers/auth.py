"""
Регистрация пользователя
Метод: POST
URL: /auth/register/

Авторизация пользователя
Метод: POST
URL: /auth/login/
"""
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from slugify import slugify
from typing import Annotated

from app.backend.db_depends import get_db
from app.schemas import UserResponse, UserCreate
from app.models.models import User, Ticket, Comment, Category
from passlib.context import CryptContext

router = APIRouter(prefix='/auth', tags=['auth'])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/register', response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, group=user.group)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post('/login')
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}



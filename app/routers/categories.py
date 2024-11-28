"""
Создание категории
Метод: POST
URL: /categories/add/
"""
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from slugify import slugify
from typing import Annotated

from app.backend.db_depends import get_db
from app.schemas import CategoryResponse, CategoryCreate
from app.models.models import User, Ticket, Comment, Category


router = APIRouter(prefix='/categories', tags=['categories'])


@router.post('/add', response_model=CategoryResponse)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = Category(name=category.name, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# # Эндпоинт создания категории
# @app.post("/categories/add/", response_model=CategoryResponse)
# def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
#     db_category = Category(name=category.name, description=category.description)
#     db.add(db_category)
#     db.commit()
#     db.refresh(db_category)
#     return db_category


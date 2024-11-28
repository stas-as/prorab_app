"""
Создание заявки
Метод: POST
URL: /tickets/add/


Получение заявки по ID
Метод: GET
URL: /tickets/{id}/

Удаление заявки
Метод: DELETE
URL: /tickets/delete/{id}/

Создание комментария к заявке
Метод: POST
URL: /tickets/{ticket_id}/comments/
"""
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from slugify import slugify
from typing import Annotated

from app.backend.db_depends import get_db
from app.schemas import TicketResponse, TicketCreate, CommentResponse, CommentCreate
from app.models.models import User, Ticket, Comment, Category

router = APIRouter(prefix='/tickets', tags=['tickets'])

@router.post('/add/', response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


@router.get('/{id}/')
def get_ticket(id: int, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket

@router.delete('/delete/{id}/')
def delete_ticket(id: int, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db.delete(db_ticket)
    db.commit()
    return {"message": "Ticket deleted successfully"}

@router.post('/{id}/comments/', response_model=CommentResponse)
def add_comment(ticket_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    db_comment = Comment(**comment.dict(), ticket_id=ticket_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


# # Эндпоинт создания тикета
# @app.post("/tickets/add/", response_model=TicketResponse)
# def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
#     db_ticket = Ticket(**ticket.dict())
#     db.add(db_ticket)
#     db.commit()
#     db.refresh(db_ticket)
#     return db_ticket

# # Эндпоинт получения тикета по ID
# @app.get("/tickets/{id}/", response_model=TicketResponse)
# def get_ticket(id: int, db: Session = Depends(get_db)):
#     db_ticket = db.query(Ticket).filter(Ticket.id == id).first()
#     if db_ticket is None:
#         raise HTTPException(status_code=404, detail="Ticket not found")
#     return db_ticket

# # Эндпоинт удаления тикета
# @app.delete("/tickets/delete/{id}/")
# def delete_ticket(id: int, db: Session = Depends(get_db)):
#     db_ticket = db.query(Ticket).filter(Ticket.id == id).first()
#     if db_ticket is None:
#         raise HTTPException(status_code=404, detail="Ticket not found")
#     db.delete(db_ticket)
#     db.commit()
#     return {"message": "Ticket deleted successfully"}

# # Эндпоинт добавления комментария к тикету
# @app.post("/tickets/{ticket_id}/comments/", response_model=CommentResponse)
# def add_comment(ticket_id: int, comment: CommentCreate, db: Session = Depends(get_db)):
#     db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
#     if db_ticket is None:
#         raise HTTPException(status_code=404, detail="Ticket not found")
#     db_comment = Comment(**comment.dict(), ticket_id=ticket_id)
#     db.add(db_comment)
#     db.commit()
#     db.refresh(db_comment)
#     return db_comment
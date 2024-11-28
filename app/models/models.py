from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.backend.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)         #почта
    password = Column(String)                               #пароль
    is_active = Column(Boolean, default=True)               #активность
    created_at = Column(DateTime, default=datetime.now())         #дата_создания
    group = Column(String)                                  #группа

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)                                               #описание
    description = Column(Text)
    status = Column(String, default="open")                                          #статус
    priority = Column(String)                                                        #приоритет
    category = Column(String)                                                        #категория
    responsible_user_id = Column(Integer, ForeignKey('users.id'))                    #ответственный
    author_user_id = Column(Integer, ForeignKey('users.id'))                         #автор
    created_at = Column(DateTime, default=datetime.now())                                  #дата_создания
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())               #дата_обновления

    responsible_user = relationship('User', foreign_keys=[responsible_user_id])
    author_user = relationship('User', foreign_keys=[author_user_id])

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    author_user_id = Column(Integer, ForeignKey('users.id'))
    ticket_id = Column(Integer, ForeignKey('tickets.id'))
    created_at = Column(DateTime, default=datetime.now())

    author_user = relationship('User')
    ticket = relationship('Ticket')

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(Text)
    
    

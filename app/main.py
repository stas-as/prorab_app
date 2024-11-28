import os
import sys
sys.path.append(os.getcwd())

from fastapi import FastAPI

from app.routers import auth
from app.routers import tickets
from app.routers import categories

from app.backend.db import engine
from sqlalchemy import MetaData

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}


app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(tickets.router)

# MetaData.create_all(engine)
# model_file.Base.metadata.create_all(bind=engine)

# alembic init async migrations
# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head  







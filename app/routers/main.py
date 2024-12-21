from fastapi import FastAPI
from app.backend.db import Base, engine
from app.models import User, Task

app = FastAPI()

# Создание всех таблиц
Base.metadata.create_all(bind=engine)

# Печать SQL-запросов
from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))

@app.get("/")
async def root():
    return {"message": "Welcome to Task Manager!"}

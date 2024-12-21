from pydantic import BaseModel
from typing import List, Optional

# Схема для Task
class TaskBase(BaseModel):
    title: str
    content: str
    priority: Optional[int] = 0
    completed: Optional[bool] = False
    slug: str

class TaskCreate(TaskBase):
    user_id: int

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True

# Схема для User
class UserBase(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    tasks: List[TaskOut] = []

    class Config:
        orm_mode = True

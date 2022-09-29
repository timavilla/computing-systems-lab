from pydantic import BaseModel
import datetime


class Order(BaseModel):
    order_name: str
    start_date: datetime.datetime

    class Config:
        orm_mode = True


class OrderGet(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Task(BaseModel):
    task_name: str
    duration: int
    resource: int
    order_id: int

    class Config:
        orm_mode = True


class TaskDependent(BaseModel):
    task_id: int

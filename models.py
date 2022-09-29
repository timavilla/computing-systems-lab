from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    order_name = Column(String)
    start_date = Column(DateTime)
    task = relationship("Task")


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String)
    duration = Column(Integer)
    resource = Column(Integer)
    order_id = Column(Integer, ForeignKey('order.id'))
    dependent = relationship("TaskDependent")


class TaskDependent(Base):
    __tablename__ = "dependent_task"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey('task.id'))

from fastapi import FastAPI
import models
from database import engine
from routers import order, task

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello tima"}

models.Base.metadata.create_all(engine)

app.include_router(order.router)
app.include_router(task.router)

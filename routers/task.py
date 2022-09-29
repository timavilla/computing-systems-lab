from fastapi import APIRouter, Depends, HTTPException
import schemas
from database import get_db

router = APIRouter()


@router.post("/task", response_model=schemas.Task)
async def create_task(request: schemas.Task):
    pass


@router.delete("/task/{id}", response_model=schemas.Task)
async def remove_task(id, request: schemas.Task):
    pass

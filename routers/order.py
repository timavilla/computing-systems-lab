from fastapi import APIRouter, Depends, HTTPException, status
import schemas
import models
from database import SessionLocal, get_db

router = APIRouter()


@router.post("/order", response_model=schemas.Order, status_code=201)
async def create_order(request: schemas.Order, db: SessionLocal = Depends(get_db)):
    new_order = models.Order(**request.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return (new_order)


@router.get("/order/{id}", response_model=schemas.OrderGet)
async def show_order(id, db: SessionLocal = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == id).first()
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='not found')
    return order


@router.put("/order/{id}", status_code=204)
async def update_order(id, request: schemas.Order, db: SessionLocal = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='not found')
    order.update(request.dict())
    db.commit()
    return {f"updated order №{id}"}


@router.delete("/order/{id}", status_code=204)
async def remove_order(id, db: SessionLocal = Depends(get_db)):
    db.query(models.Order).filter(models.Order.id == id).delete()
    return {f"deleted order №{id}"}

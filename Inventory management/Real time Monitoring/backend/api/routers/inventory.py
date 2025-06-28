from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas
from typing import List

router = APIRouter(prefix="/inventory", tags=["inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("", response_model=List[schemas.InventoryItem])
def list_inventory(db: Session = Depends(get_db)):
    return crud.get_inventory_items(db)

@router.post("", response_model=schemas.InventoryItem)
def add_inventory(item: schemas.InventoryItemCreate, db: Session = Depends(get_db)):
    return crud.create_inventory_item(db, item)

@router.get("/{item_id}", response_model=schemas.InventoryItem)
def get_inventory(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_inventory_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.InventoryItem)
def update_inventory(item_id: int, quantity: int, db: Session = Depends(get_db)):
    db_item = crud.update_inventory_item(db, item_id, quantity)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}")
def delete_inventory(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_inventory_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"} 
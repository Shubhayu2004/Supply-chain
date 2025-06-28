from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime

def create_detection_result(db: Session, result: schemas.DetectionResultCreate):
    db_result = models.DetectionResult(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_detection_result(db: Session, result_id: int):
    return db.query(models.DetectionResult).filter(models.DetectionResult.id == result_id).first()

def get_detection_results(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DetectionResult).offset(skip).limit(limit).all()

def create_inventory_item(db: Session, item: schemas.InventoryItemCreate):
    db_item = models.InventoryItem(**item.dict(), last_updated=datetime.utcnow())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_inventory_item(db: Session, item_id: int):
    return db.query(models.InventoryItem).filter(models.InventoryItem.id == item_id).first()

def get_inventory_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.InventoryItem).offset(skip).limit(limit).all()

def update_inventory_item(db: Session, item_id: int, quantity: int):
    db_item = get_inventory_item(db, item_id)
    if db_item:
        db_item.quantity = quantity
        db_item.last_updated = datetime.utcnow()
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_inventory_item(db: Session, item_id: int):
    db_item = get_inventory_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item 
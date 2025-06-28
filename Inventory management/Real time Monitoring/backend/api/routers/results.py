from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas
from typing import List

router = APIRouter(prefix="/results", tags=["results"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{result_id}", response_model=schemas.DetectionResult)
def get_result(result_id: int, db: Session = Depends(get_db)):
    db_result = crud.get_detection_result(db, result_id)
    if not db_result:
        raise HTTPException(status_code=404, detail="Result not found")
    return db_result

@router.get("", response_model=List[schemas.DetectionResult])
def list_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_detection_results(db, skip=skip, limit=limit) 
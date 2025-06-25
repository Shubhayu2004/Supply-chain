from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class DetectionResultBase(BaseModel):
    filename: str
    detected_classes: str  # JSON string or comma-separated
    result_image_path: str

class DetectionResultCreate(DetectionResultBase):
    pass

class DetectionResult(DetectionResultBase):
    id: int
    timestamp: datetime
    class Config:
        orm_mode = True

class InventoryItemBase(BaseModel):
    name: str
    quantity: int

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItem(InventoryItemBase):
    id: int
    last_updated: datetime
    class Config:
        orm_mode = True 
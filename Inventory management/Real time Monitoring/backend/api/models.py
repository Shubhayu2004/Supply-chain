from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from database import Base
import datetime

class DetectionResult(Base):
    __tablename__ = "detection_results"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    detected_classes = Column(Text)  # JSON string or comma-separated
    result_image_path = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class InventoryItem(Base):
    __tablename__ = "inventory_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    quantity = Column(Integer, default=0)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow) 
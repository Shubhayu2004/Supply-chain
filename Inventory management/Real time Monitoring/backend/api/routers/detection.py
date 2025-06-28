from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas, yolov8, utils

router = APIRouter(prefix="/detect", tags=["detection"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/image", response_model=schemas.DetectionResult)
def detect_image(
    file: UploadFile = File(None),
    base64_image: str = Form(None),
    db: Session = Depends(get_db)
):
    if not file and not base64_image:
        raise HTTPException(status_code=400, detail="No image provided.")
    if file:
        image_path = utils.save_upload_file(file)
        filename = file.filename
    else:
        image_path = utils.save_base64_image(base64_image)
        filename = "camera_image.jpg"
    infer_result = yolov8.run_inference(image_path)
    result_in = schemas.DetectionResultCreate(
        filename=filename,
        detected_classes=infer_result['detected_classes'],
        result_image_path=infer_result['result_image_path']
    )
    db_result = crud.create_detection_result(db, result_in)
    return db_result

@router.post("/video")
def detect_video():
    return {"message": "Video detection endpoint (to be implemented)"} 
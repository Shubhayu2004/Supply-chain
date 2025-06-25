from fastapi import APIRouter

router = APIRouter(prefix="/detect", tags=["detection"])

@router.post("/image")
def detect_image():
    return {"message": "Image detection endpoint (to be implemented)"}

@router.post("/video")
def detect_video():
    return {"message": "Video detection endpoint (to be implemented)"} 
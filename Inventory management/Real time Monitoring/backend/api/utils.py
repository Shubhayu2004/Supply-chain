import base64
import uuid
import os
from fastapi import UploadFile

UPLOAD_DIR = os.path.join(os.path.dirname(__file__), '../uploads')
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_file(upload_file: UploadFile) -> str:
    file_ext = os.path.splitext(upload_file.filename)[-1]
    file_id = uuid.uuid4().hex
    file_path = os.path.join(UPLOAD_DIR, f"upload_{file_id}{file_ext}")
    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())
    return file_path

def save_base64_image(base64_str: str) -> str:
    file_id = uuid.uuid4().hex
    file_path = os.path.join(UPLOAD_DIR, f"camera_{file_id}.jpg")
    with open(file_path, "wb") as f:
        f.write(base64.b64decode(base64_str))
    return file_path 
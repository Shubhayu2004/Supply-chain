from ultralytics import YOLO
from PIL import Image
import os
import uuid

# Load the trained YOLOv8 model (update path if needed)
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../Notebooks/runs/detect/train/weights/best.pt')

# Check if model file exists, if not use a default YOLO model
if os.path.exists(MODEL_PATH):
    model = YOLO(MODEL_PATH)
else:
    print(f"Warning: Model file not found at {MODEL_PATH}")
    print("Using default YOLOv8n model instead.")
    model = YOLO('yolov8n.pt')  # Use a default model as fallback

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '../results')
os.makedirs(RESULTS_DIR, exist_ok=True)

def run_inference(image_path: str):
    results = model(image_path)
    # Save result image with bounding boxes
    result_img_path = os.path.join(RESULTS_DIR, f"result_{uuid.uuid4().hex}.jpg")
    results[0].save(result_img_path)
    # Get detected class names
    detected_classes = ','.join([model.names[int(cls)] for cls in results[0].boxes.cls.cpu().numpy()])
    return {
        'result_image_path': result_img_path,
        'detected_classes': detected_classes
    } 
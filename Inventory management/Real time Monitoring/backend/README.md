# Inventory Monitoring Backend

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn api.app:app --reload
   ```

## Features
- Run YOLOv8 inference on images/videos
- Store and serve detection results
- Inventory CRUD operations
- API endpoints for frontend integration 
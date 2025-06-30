# Real-Time Inventory Monitoring System

A complete inventory monitoring system with YOLOv8 object detection, FastAPI backend, and React frontend.

## Project Structure

```
Real time Monitoring/
├── backend/                 # FastAPI backend
│   ├── api/
│   │   ├── app.py          # Main FastAPI application
│   │   ├── database.py     # Database configuration
│   │   ├── models.py       # SQLAlchemy models
│   │   ├── schemas.py      # Pydantic schemas
│   │   ├── crud.py         # CRUD operations
│   │   ├── yolov8.py       # YOLO inference logic
│   │   ├── utils.py        # Utility functions
│   │   └── routers/        # API route handlers
│   │       ├── detection.py
│   │       ├── results.py
│   │       └── inventory.py
│   ├── requirements.txt    # Python dependencies
│   ├── init_db.py         # Database initialization script
│   └── README.md          # Backend documentation
├── frontend/              # React frontend
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── components/
│   │       ├── DetectionForm.js
│   │       ├── ResultsList.js
│   │       └── InventoryManager.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── README.md
├── Data/                  # Training data and models
│   ├── train/
│   ├── valid/
│   ├── test/
│   └── README.dataset.txt
├── Notebooks/            # Jupyter notebooks
│   ├── Data Exploration.ipynb
│   ├── Model_Development.ipynb
│   └── runs/
│       └── detect/
│           └── train/
│               └── weights/
│                   ├── best.pt    # Trained YOLO model
│                   └── last.pt
└── README.md            # This file
```

## Features

- **Object Detection**: YOLOv8 model for real-time inventory item detection
- **Image Upload**: Support for file uploads and camera capture
- **Results Storage**: Database storage for detection results
- **Inventory Management**: CRUD operations for inventory items
- **API Documentation**: Auto-generated Swagger UI
- **CORS Support**: Cross-origin requests for frontend integration

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

## Quick Start

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Initialize the database
python init_db.py

# Start the FastAPI server
cd api
uvicorn app:app --reload
```

The backend will be available at:
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will be available at http://localhost:3000

## API Endpoints

### Detection
- `POST /detect/image` - Upload image for detection (file or base64)
- `POST /detect/video` - Video detection (placeholder)

### Results
- `GET /results` - List all detection results
- `GET /results/{id}` - Get specific detection result

### Inventory
- `GET /inventory` - List all inventory items
- `POST /inventory` - Add new inventory item
- `GET /inventory/{id}` - Get specific inventory item
- `PUT /inventory/{id}` - Update inventory item quantity
- `DELETE /inventory/{id}` - Delete inventory item

## Usage

### 1. Start Both Services

**Terminal 1 (Backend):**
```bash
cd backend/api
uvicorn app:app --reload
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm start
```

### 2. Using the Application

1. **Open the frontend** at http://localhost:3000
2. **Upload an image** or **use camera** to detect inventory items
3. **View detection results** in the results section
4. **Manage inventory** by adding, updating, or deleting items

### 3. API Testing

Visit http://localhost:8000/docs to:
- Test API endpoints directly
- View request/response schemas
- Upload images for testing

## Configuration

### Model Path
The system looks for the trained YOLO model at:
```
Notebooks/runs/detect/train/weights/best.pt
```

If the model is not found, it falls back to the default YOLOv8n model.

### Database
- **Type**: SQLite
- **Location**: `backend/inventory.db`
- **Tables**: `detection_results`, `inventory_items`

### CORS
The backend allows requests from any origin (`*`) for development. In production, specify your frontend URL.

## Development

### Adding New Features

1. **Backend**: Add new routes in `backend/api/routers/`
2. **Frontend**: Add new components in `frontend/src/components/`
3. **Database**: Update models in `backend/api/models.py`

### File Structure
- **Uploads**: Stored in `backend/uploads/`
- **Results**: Stored in `backend/results/`
- **Static Files**: Served from `backend/results/` at `/results/`

## Troubleshooting

### Common Issues

1. **Database Tables Not Found**
   ```bash
   cd backend
   python init_db.py
   ```

2. **Model Not Found**
   - Ensure the trained model exists at the specified path
   - The system will use a default model if not found

3. **CORS Errors**
   - Backend CORS is configured to allow all origins
   - Check that the backend is running on port 8000

4. **Port Conflicts**
   - Backend: Change port in uvicorn command
   - Frontend: Change port in package.json scripts

### Logs
- **Backend**: Check terminal output for FastAPI logs
- **Frontend**: Check browser console for React errors

## Production Deployment

### Backend
- Use a production ASGI server (Gunicorn + Uvicorn)
- Configure proper CORS origins
- Use a production database (PostgreSQL, MySQL)
- Set up proper environment variables

### Frontend
- Build for production: `npm run build`
- Serve static files with a web server (Nginx, Apache)
- Configure API endpoint URLs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and development purposes.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the API documentation at http://localhost:8000/docs
3. Check the browser console for frontend errors 
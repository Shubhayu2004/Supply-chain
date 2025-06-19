
"""
Sales Forecasting API Documentation

Endpoints:
---------
1. POST /api/v1/predict
   Generate sales forecasts for a specific item
   
   Request Body:
   {
       "item_id": "string",
       "forecast_days": integer (optional, default=7)
   }

2. GET /api/v1/model-info
   Get information about available models
"""

# Supply Chain Sales Forecasting System

## Overview
This project implements a machine learning-based sales forecasting system using multiple models (SARIMA, XGBoost, and Holt-Winters) with a Flask backend API and React frontend interface.

## Project Structure
```
supply-chain/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── middleware.py
│   ├── models/
│   │   ├── saved/
│   │   ├── __init__.py
│   │   └── sales_model.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── validators.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_api.py
│   ├── config.py
│   └── app.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── config/
│   │   └── App.tsx
│   ├── .env
│   └── package.json
└── README.md
```

## Features
- Multi-model ensemble forecasting
- RESTful API endpoints
- Interactive visualization
- TypeScript-based frontend
- Automated testing

## Installation

### Backend Setup
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd frontend
npm install
```

## Environment Configuration

### Backend
Create a `config.py` file in the backend directory:
````python
DEBUG = True
PORT = 5000
HOST = '0.0.0.0'
````

### Frontend
Create `.env` file in the frontend directory:
````properties
REACT_APP_API_URL=http://localhost:5000/api/v1
````

## Running the Application

### Start Backend Server
```bash
cd backend
.\venv\Scripts\activate
python app.py
```

### Start Frontend Development Server
```bash
cd frontend
npm start
```

## API Endpoints

### Predict Sales
- **URL**: `/api/v1/predict`
- **Method**: POST
- **Body**:
```json
{
    "item_id": "string",
    "forecast_days": integer
}
```

### Model Information
- **URL**: `/api/v1/model-info`
- **Method**: GET

## Testing

### Backend Tests
```bash
cd backend
python -m unittest discover tests
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Model Information
The system uses three forecasting models:
1. SARIMA - For capturing seasonal patterns
2. XGBoost - For non-linear relationships
3. Holt-Winters - For trend and seasonality

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License

## Authors
[Your Name]

## Acknowledgments
- statsmodels
- XGBoost
- React
- Flask

## Troubleshooting
- Ensure all dependencies are installed
- Check port availability (5000 for backend, 3000 for frontend)
- Verify environment variables
- Check model files exist in backend/models/saved/

For more detailed information, please refer to the documentation in each component's directory.
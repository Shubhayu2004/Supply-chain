
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
"""e
from flask import request, jsonify
from models.sales_model import SalesPredictor
from utils.data_preprocessing import preprocess_data, create_features
from models.model_utils import prepare_forecast_output
import pandas as pd

def handle_predict_request():
    """
    Handle prediction request and return formatted response
    """
    try:
        data = request.get_json()
        item_id = data.get('item_id')
        forecast_days = data.get('forecast_days', 30)
        
        # Initialize predictor
        predictor = SalesPredictor()
        
        # Generate forecast
        forecast = predictor.predict(item_id, forecast_days)
        
        # Generate forecast dates
        last_date = pd.Timestamp.now()
        forecast_dates = pd.date_range(last_date, periods=forecast_days)
        
        # Prepare response
        forecast_data = prepare_forecast_output(forecast, forecast_dates)
        
        return jsonify({
            'status': 'success',
            'forecast': forecast_data,
            'message': 'Forecast generated successfully'
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
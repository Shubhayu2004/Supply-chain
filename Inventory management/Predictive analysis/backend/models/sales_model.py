import joblib
import pandas as pd
from config import SARIMA_MODEL_PATH, XGB_MODEL_PATH, HW_MODEL_PATH

class SalesPredictor:
    def __init__(self):
        self.sarima_model = joblib.load(SARIMA_MODEL_PATH)
        self.xgb_model = joblib.load(XGB_MODEL_PATH)
        self.hw_model = joblib.load(HW_MODEL_PATH)
    
    def predict(self, item_id, forecast_days=30):
        """Generate sales forecast for specific item"""
        # Use SARIMA as default model
        forecast = self.sarima_model.forecast(steps=forecast_days)
        return forecast
    
    def get_model_info(self):
        """Return information about loaded models"""
        return {
            'models_available': ['SARIMA', 'XGBoost', 'Holt-Winters'],
            'sarima_params': str(self.sarima_model.specification),
            'last_trained': 'placeholder_date'
        }
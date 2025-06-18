import joblib
import pandas as pd
import numpy as np

class SalesPredictor:
    def __init__(self):
        # Initialize with dummy models for testing
        self.sarima_model = DummyModel()
        self.xgb_model = DummyModel()
        self.hw_model = DummyModel()
    
    def predict(self, item_id, forecast_days=30):
        """Generate sales forecast for specific item"""
        # For testing, return dummy forecast
        return np.random.rand(forecast_days)
    
    def get_model_info(self):
        """Return information about loaded models"""
        return {
            'models_available': ['SARIMA', 'XGBoost', 'Holt-Winters'],
            'sarima_params': 'dummy_params',
            'last_trained': '2023-01-01'
        }

class DummyModel:
    """Dummy model class for testing"""
    def __init__(self):
        self.specification = "dummy_spec"
    
    def forecast(self, steps):
        return np.random.rand(steps)
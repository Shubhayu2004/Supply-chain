import joblib
import numpy as np
import os

class SalesPredictor:
    def __init__(self):
        self.model_dir = os.path.join(os.path.dirname(__file__), 'saved')
        self.sarima_model = joblib.load(os.path.join(self.model_dir, 'sarima_model.joblib'))
        self.xgb_model = joblib.load(os.path.join(self.model_dir, 'xgb_model.joblib'))
        self.hw_model = joblib.load(os.path.join(self.model_dir, 'hw_model.joblib'))

    def predict(self, brand, description, forecast_days=7):
        # In a real implementation, you would filter your data for this brand/description
        # and generate features for the models. Here, we just use the models as-is.
        sarima_forecast = self.sarima_model.forecast(steps=forecast_days)
        features = np.zeros((forecast_days, self.xgb_model.n_features_in_))
        xgb_forecast = self.xgb_model.predict(features)
        hw_forecast = self.hw_model.forecast(forecast_days)
        ensemble = np.mean([sarima_forecast, xgb_forecast, hw_forecast], axis=0)
        return {
            'forecast': ensemble.tolist(),
            'individual_forecasts': {
                'sarima': sarima_forecast.tolist(),
                'xgboost': xgb_forecast.tolist(),
                'holtwinters': hw_forecast.tolist()
            }
        }

    def get_model_info(self):
        """Get information about the models"""
        return {
            'models_available': ['SARIMA', 'XGBoost', 'Holt-Winters'],
            'models_loaded': True,
            'last_trained': '2023-01-01'  # Placeholder date
        }
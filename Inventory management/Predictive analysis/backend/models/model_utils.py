import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def calculate_metrics(y_true, y_pred):
    """
    Calculate common forecasting metrics
    """
    metrics = {
        'mae': mean_absolute_error(y_true, y_pred),
        'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
        'mape': np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    }
    return metrics

def prepare_forecast_output(forecast, dates):
    """
    Prepare forecast results for API response
    """
    return {
        'dates': dates.tolist(),
        'values': forecast.tolist(),
        'lower_bound': (forecast - forecast * 0.1).tolist(),  # Simple 90% confidence interval
        'upper_bound': (forecast + forecast * 0.1).tolist()
    }
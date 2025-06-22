import joblib
import numpy as np
import pandas as pd
import os

class SalesPredictor:
    def __init__(self):
        self.model_dir = os.path.join(os.path.dirname(__file__), 'saved')
        self.sarima_model = joblib.load(os.path.join(self.model_dir, 'sarima_model.joblib'))
        self.xgb_model = joblib.load(os.path.join(self.model_dir, 'xgb_model.joblib'))
        self.hw_model = joblib.load(os.path.join(self.model_dir, 'hw_model.joblib'))
        # Load sales data
        data_path = os.path.join(os.path.dirname(__file__), "synthetic_sales_2_years.csv")
        self.sales_data = pd.read_csv(data_path, parse_dates=['SalesDate'])
        self.item_daily_sales = self.sales_data.groupby(['SalesDate', 'Brand', 'Description'])['SalesQuantity'].sum().reset_index()
        self.item_daily_sales['Brand'] = self.item_daily_sales['Brand'].astype(str).str.strip().str.lower()
        self.item_daily_sales['Description'] = self.item_daily_sales['Description'].astype(str).str.strip().str.lower()

    def prepare_item_series(self, brand, description):
        brand = brand.strip().lower()
        description = description.strip().lower()
        item_series = self.item_daily_sales[
            (self.item_daily_sales['Brand'] == brand) &
            (self.item_daily_sales['Description'] == description)
        ].set_index('SalesDate')['SalesQuantity']
        if item_series.empty:
            raise ValueError("No sales data for this item.")
        idx = pd.date_range(item_series.index.min(), item_series.index.max())
        item_series = item_series.reindex(idx, fill_value=0)
        return item_series

    def create_item_features(self, series):
        df = pd.DataFrame(index=series.index)
        df['sales'] = series
        df['year'] = df.index.year
        df['month'] = df.index.month
        df['day'] = df.index.day
        df['day_of_week'] = df.index.dayofweek
        df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
        # Lag features
        df['sales_lag1'] = df['sales'].shift(1)
        df['sales_lag7'] = df['sales'].shift(7)
        # Rolling statistics
        df['rolling_mean_7'] = df['sales'].rolling(7).mean()
        df['rolling_max_7'] = df['sales'].rolling(7).max()
        df['rolling_std_7'] = df['sales'].rolling(7).std()
        df = df.dropna()
        return df

    def forecast_xgboost(self, features_df, forecast_days):
        feature_names = [
            'year', 'month', 'day', 'day_of_week',
            'lag_1', 'lag_7', 'lag_14',
            'rolling_mean_7', 'rolling_std_7',
            'rolling_mean_14', 'rolling_std_14',
            'rolling_mean_30', 'rolling_std_30'
        ]
        
        last_known = features_df.iloc[-1].copy()
        last_date = features_df.index[-1]  # ✅ Initialize here
        
        preds = []
        sales_hist = list(features_df['sales'].values)
        
        for i in range(forecast_days):
            # Update lag features
            last_known['lag_1'] = sales_hist[-1] if len(sales_hist) >= 1 else 0
            last_known['lag_7'] = sales_hist[-7] if len(sales_hist) >= 7 else 0
            last_known['lag_14'] = sales_hist[-14] if len(sales_hist) >= 14 else 0
            
            # Update rolling features
            last7 = sales_hist[-7:] if len(sales_hist) >= 7 else sales_hist
            last14 = sales_hist[-14:] if len(sales_hist) >= 14 else sales_hist
            last30 = sales_hist[-30:] if len(sales_hist) >= 30 else sales_hist
            
            last_known['rolling_mean_7'] = np.mean(last7) if last7 else 0
            last_known['rolling_std_7'] = np.std(last7) if len(last7) > 1 else 0
            last_known['rolling_mean_14'] = np.mean(last14) if last14 else 0
            last_known['rolling_std_14'] = np.std(last14) if len(last14) > 1 else 0
            last_known['rolling_mean_30'] = np.mean(last30) if last30 else 0
            last_known['rolling_std_30'] = np.std(last30) if len(last30) > 1 else 0
            
            # Update time-based features using the date
            last_date += pd.Timedelta(days=1)
            last_known['year'] = last_date.year
            last_known['month'] = last_date.month
            last_known['day'] = last_date.day
            last_known['day_of_week'] = last_date.dayofweek
            
            # Predict
            X_pred = last_known[feature_names].values.reshape(1, -1)
            pred = self.xgb_model.predict(X_pred)[0]
            preds.append(pred)
            sales_hist.append(pred)
            
        return np.array(preds)

    def predict(self, brand, description, forecast_days=7):
        # Prepare item series
        item_series = self.prepare_item_series(brand, description)
        features_df = self.create_item_features(item_series)
        if features_df.empty:
            raise ValueError("Not enough data to generate features for this item.")
        # SARIMA forecast
        sarima_forecast = self.sarima_model.forecast(steps=forecast_days)
        # XGBoost forecast (rolling)
        xgb_forecast = self.forecast_xgboost(features_df, forecast_days)
        # Holt-Winters forecast
        hw_forecast = self.hw_model.forecast(forecast_days)
        # Ensemble
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
        return {
            'models_available': ['SARIMA', 'XGBoost', 'Holt-Winters'],
            'models_loaded': True,
            'last_trained': '22-06-2025'
        }
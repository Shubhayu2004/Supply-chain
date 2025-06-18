import pandas as pd
import numpy as np

def preprocess_data(data, item_id=None):
    """
    Preprocess input data for time series forecasting
    """
    try:
        # Convert to DataFrame if necessary
        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data)
            
        # Convert date columns
        if 'SalesDate' in data.columns:
            data['SalesDate'] = pd.to_datetime(data['SalesDate'])
            
        # Filter by item_id if provided
        if item_id and 'Brand' in data.columns:
            data = data[data['Brand'] == item_id]
            
        # Aggregate daily sales if needed
        if 'SalesQuantity' in data.columns:
            daily_sales = data.groupby('SalesDate')['SalesQuantity'].sum().reset_index()
            daily_sales = daily_sales.set_index('SalesDate')
            
        return daily_sales
        
    except Exception as e:
        raise ValueError(f"Error in data preprocessing: {str(e)}")

def create_features(series):
    """
    Create time series features for modeling
    """
    df = pd.DataFrame(index=series.index)
    df['sales'] = series
    
    # Time based features
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['day'] = df.index.day
    df['day_of_week'] = df.index.dayofweek
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    
    # Lag features
    df['sales_lag1'] = df['sales'].shift(1)
    df['sales_lag7'] = df['sales'].shift(7)
    
    # Rolling features
    df['rolling_mean_7'] = df['sales'].rolling(7).mean()
    df['rolling_std_7'] = df['sales'].rolling(7).std()
    
    return df.dropna()
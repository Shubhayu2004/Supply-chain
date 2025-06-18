import os

# Flask settings
DEBUG = True
PORT = 5000

# Model paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models', 'saved')
SARIMA_MODEL_PATH = os.path.join(MODEL_DIR, 'sarima_model.joblib')
XGB_MODEL_PATH = os.path.join(MODEL_DIR, 'xgb_model.joblib')
HW_MODEL_PATH = os.path.join(MODEL_DIR, 'hw_model.joblib')

# Data settings
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
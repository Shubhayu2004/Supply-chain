from flask import Blueprint, request, jsonify
from models.sales_model import SalesPredictor
from utils.validators import validate_predict_input
from .middleware import handle_errors
import os
import pandas as pd

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    item_id = data.get('item_id')
    forecast_days = int(data.get('forecast_days', 7))
    if not item_id or '|' not in item_id:
        return jsonify({'status': 'error', 'message': 'Invalid item_id'}), 400
    brand, description = item_id.split('|', 1)
    predictor = SalesPredictor()
    result = predictor.predict(brand, description, forecast_days)
    return jsonify({
        'status': 'success',
        'forecast': result['forecast'],
        'individual_forecasts': result['individual_forecasts']
    }), 200

@api_blueprint.route('/model-info', methods=['GET'])
@handle_errors
def model_info():
    predictor = SalesPredictor()
    info = predictor.get_model_info()
    return jsonify({
        'status': 'success',
        'info': info
    }), 200

@api_blueprint.route('/items', methods=['GET'])
def get_items():
    # Adjust the path to your data file as needed
    data_path = os.path.join(os.path.dirname(__file__), '../models/synthetic_sales_2_years.csv')
    df = pd.read_csv(data_path)
    df['Brand'] = df['Brand'].astype(str).str.strip().str.lower()
    df['Description'] = df['Description'].astype(str).str.strip().str.lower()
    df['item_id'] = df['Brand'] + '|' + df['Description']
    items = df[['item_id', 'Brand', 'Description']].drop_duplicates().to_dict(orient='records')
    return jsonify(items)

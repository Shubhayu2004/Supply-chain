from flask import Blueprint, request, jsonify
from models.sales_model import SalesPredictor
from utils.validators import validate_predict_input
from .middleware import handle_errors

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/predict', methods=['POST'])
@handle_errors
def predict():
    data = request.get_json()
    is_valid, error = validate_predict_input(data)
    
    if not is_valid:
        return jsonify({
            'status': 'error',
            'message': error
        }), 400
        
    predictor = SalesPredictor()
    result = predictor.predict(
        item_id=data['item_id'],
        forecast_days=data.get('forecast_days', 7)
    )
    
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
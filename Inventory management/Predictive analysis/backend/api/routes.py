from flask import Blueprint, request, jsonify
from models.sales_model import SalesPredictor

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/model-info', methods=['GET'])
def model_info():
    try:
        predictor = SalesPredictor()
        info = predictor.get_model_info()
        return jsonify({
            'status': 'success',
            'info': info
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@api_blueprint.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        item_id = data.get('item_id')
        forecast_days = int(data.get('forecast_days', 7))
        
        predictor = SalesPredictor()
        result = predictor.predict(item_id, forecast_days)
        
        return jsonify({
            'status': 'success',
            'forecast': result['forecast'],
            'individual_forecasts': result['individual_forecasts']
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400
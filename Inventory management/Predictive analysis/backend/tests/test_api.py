import unittest
import json
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_predict_endpoint(self):
        test_data = {
            "item_id": "1004",
            "forecast_days": 7
        }
        response = self.app.post(
            '/api/v1/predict',
            data=json.dumps(test_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data['forecast']), 7)
        self.assertIn('individual_forecasts', data)
        
    def test_model_info_endpoint(self):
        response = self.app.get('/api/v1/model-info')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('info', data)
        self.assertIn('models_available', data['info'])

if __name__ == '__main__':
    unittest.main()
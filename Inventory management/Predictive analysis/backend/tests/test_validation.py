import unittest
from utils.validators import validate_predict_input

class TestValidation(unittest.TestCase):
    def test_valid_input(self):
        data = {"item_id": "1004", "forecast_days": 7}
        is_valid, error = validate_predict_input(data)
        self.assertTrue(is_valid)
        self.assertEqual(error, "")
    
    def test_invalid_forecast_days(self):
        data = {"item_id": "1004", "forecast_days": -1}
        is_valid, error = validate_predict_input(data)
        self.assertFalse(is_valid)
        self.assertIn("between 1 and 365", error)

if __name__ == '__main__':
    unittest.main()
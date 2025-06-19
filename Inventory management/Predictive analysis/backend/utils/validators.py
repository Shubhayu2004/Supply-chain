from typing import Dict, Any, Tuple

def validate_predict_input(data: Dict[str, Any]) -> Tuple[bool, str]:
    """Validate prediction request input"""
    if not data:
        return False, "No input data provided"
    
    if 'item_id' not in data:
        return False, "item_id is required"
        
    if 'forecast_days' in data:
        try:
            days = int(data['forecast_days'])
            if days <= 0 or days > 365:
                return False, "forecast_days must be between 1 and 365"
        except ValueError:
            return False, "forecast_days must be a valid integer"
            
    return True, ""
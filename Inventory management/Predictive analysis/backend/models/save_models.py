import joblib
import os

def save_models(sarima_model, xgb_model, hw_model):
    """Save models with proper XGBoost handling"""
    model_dir = os.path.join(os.path.dirname(__file__), 'saved')
    os.makedirs(model_dir, exist_ok=True)
    
    # Save SARIMA and Holt-Winters models
    joblib.dump(sarima_model, os.path.join(model_dir, 'sarima_model.joblib'))
    joblib.dump(hw_model, os.path.join(model_dir, 'hw_model.joblib'))
    
    # Save XGBoost model properly
    xgb_path = os.path.join(model_dir, 'xgb_model.json')
    model_path = os.path.join(model_dir, 'xgb_model.joblib')
    xgb_model.save_model(xgb_path)  # Save model in XGBoost format
    joblib.dump(xgb_model, model_path)  # Also save pickle for compatibility
    
    print("Models saved successfully!")
import os
import joblib

def check_model_files():
    """Debug utility to check model files"""
    model_dir = os.path.join(os.path.dirname(__file__), '..', 'models', 'saved')
    model_files = ['sarima_model.joblib', 'xgb_model.joblib', 'hw_model.joblib']
    
    print(f"Checking model directory: {model_dir}")
    print(f"Directory exists: {os.path.exists(model_dir)}\n")
    
    for file in model_files:
        file_path = os.path.join(model_dir, file)
        print(f"Checking {file}:")
        print(f"File exists: {os.path.exists(file_path)}")
        if os.path.exists(file_path):
            try:
                model = joblib.load(file_path)
                print(f"Successfully loaded model: {type(model)}")
            except Exception as e:
                print(f"Error loading model: {str(e)}")
        print()

if __name__ == "__main__":
    check_model_files()
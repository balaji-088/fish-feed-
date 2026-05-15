import joblib
import pandas as pd
import os
from src.utils import get_logger

logger = get_logger('inference')

class FishFeedPredictor:
    def __init__(self, models_path='models'):
        self.rf_model = joblib.load(os.path.join(models_path, 'rf_model.joblib'))
        self.xgb_model = joblib.load(os.path.join(models_path, 'xgb_model.joblib'))
        self.preprocessor = joblib.load(os.path.join(models_path, 'preprocessor.joblib'))
        
    def predict(self, input_data: dict):
        """
        Predicts feed quantity for a single input.
        Input data should contain: ph, temperature, turbidity, fish, Fish_Weight
        """
        df = pd.DataFrame([input_data])
        X = df[['ph', 'temperature', 'turbidity', 'fish', 'Fish_Weight']]
        
        X_processed = self.preprocessor.transform(X)
        
        rf_pred = self.rf_model.predict(X_processed)[0]
        xgb_pred = self.xgb_model.predict(X_processed)[0]
        
        # Ensemble: 60% RF, 40% XGB
        feed_ratio = (0.6 * rf_pred) + (0.4 * xgb_pred)
        
        # Convert ratio back to Feed quantity
        feed_quantity = feed_ratio * input_data['Fish_Weight']
        
        return {
            "feed_ratio": float(feed_ratio),
            "feed_quantity": float(feed_quantity)
        }

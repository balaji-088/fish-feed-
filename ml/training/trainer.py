import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from ml.training.preprocessor import get_preprocessing_pipeline
import joblib
import os
from src.utils import get_logger

logger = get_logger('trainer')

class FishFeedTrainer:
    def __init__(self, model_save_path='models'):
        self.model_save_path = model_save_path
        if not os.path.exists(model_save_path):
            os.makedirs(model_save_path)
            
    def train(self, df: pd.DataFrame):
        """Trains the ensemble model."""
        logger.info("Preparing data for training...")
        
        X = df[['ph', 'temperature', 'turbidity', 'fish', 'Fish_Weight']]
        y = df['feed_ratio']
        
        categorical_features = ['fish']
        numerical_features = ['ph', 'temperature', 'turbidity', 'Fish_Weight']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Preprocessing
        preprocessor = get_preprocessing_pipeline(categorical_features, numerical_features)
        X_train_processed = preprocessor.fit_transform(X_train)
        X_test_processed = preprocessor.transform(X_test)
        
        # Models
        logger.info("Training Random Forest...")
        rf = RandomForestRegressor(n_estimators=100, random_state=42)
        rf.fit(X_train_processed, y_train)
        
        logger.info("Training XGBoost...")
        xgb = XGBRegressor(n_estimators=100, random_state=42)
        xgb.fit(X_train_processed, y_train)
        
        # Save models and preprocessor
        joblib.dump(rf, os.path.join(self.model_save_path, 'rf_model.joblib'))
        joblib.dump(xgb, os.path.join(self.model_save_path, 'xgb_model.joblib'))
        joblib.dump(preprocessor, os.path.join(self.model_save_path, 'preprocessor.joblib'))
        
        logger.info("Models saved successfully.")
        
        return rf, xgb, preprocessor, X_test_processed, y_test

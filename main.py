from src.utils import setup_logging, get_logger
from src.data_eng.loader import DataLoader
from src.data_eng.transformer import DataTransformer
from ml.training.trainer import FishFeedTrainer
from ml.evaluation.evaluator import ModelEvaluator
from ml.evaluation.feature_analysis import analyze_feature_importance
import os

def run_pipeline():
    # Setup
    logger = setup_logging()
    logger.info("Starting Fish Feed Prediction Pipeline...")
    
    # 1. Load Data
    loader = DataLoader('data/fish_dataset.csv')
    df_raw = loader.load_data()
    
    # 2. Transform Data
    transformer = DataTransformer()
    df_transformed = transformer.transform(df_raw)
    
    # 3. Train Models
    trainer = FishFeedTrainer()
    rf, xgb, preprocessor, X_test, y_test = trainer.train(df_transformed)
    
    # 4. Evaluate
    evaluator = ModelEvaluator()
    metrics = evaluator.evaluate(rf, xgb, X_test, y_test)
    
    # 5. Feature Importance
    analyze_feature_importance(rf, preprocessor, [])
    
    logger.info("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()

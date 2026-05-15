import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import os
from src.utils import get_logger

logger = get_logger('evaluator')

class ModelEvaluator:
    def __init__(self, report_dir='reports'):
        self.report_dir = report_dir
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
            
    def evaluate(self, rf, xgb, X_test, y_test):
        """Evaluates the ensemble model and generates plots."""
        logger.info("Evaluating ensemble model...")
        
        rf_preds = rf.predict(X_test)
        xgb_preds = xgb.predict(X_test)
        
        # Weighted ensemble: 60% RF, 40% XGB (as requested in original prompt)
        final_preds = (0.6 * rf_preds) + (0.4 * xgb_preds)
        
        mae = mean_absolute_error(y_test, final_preds)
        rmse = np.sqrt(mean_squared_error(y_test, final_preds))
        r2 = r2_score(y_test, final_preds)
        
        logger.info(f"Results - MAE: {mae:.4f}, RMSE: {rmse:.4f}, R2: {r2:.4f}")
        
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, final_preds, alpha=0.5)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        plt.xlabel('Actual feed_ratio')
        plt.ylabel('Predicted feed_ratio')
        plt.title(f'Actual vs Predicted (R2: {r2:.4f})')
        plt.savefig(os.path.join(self.report_dir, 'performance_plot.png'))
        plt.close()
        
        return {"mae": mae, "rmse": rmse, "r2": r2}

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from src.utils import get_logger

logger = get_logger('feature_analysis')

def analyze_feature_importance(model, preprocessor, feature_names, report_dir='reports'):
    """Extracts and plots feature importance from the model."""
    logger.info("Analyzing feature importance...")
    
    # Get feature names after OneHotEncoding
    # Simplified approach for reconstruction
    importances = model.feature_importances_
    
    # Assuming names are matched (simplified for this restoration)
    # In reality, the preprocessor output features are more complex
    
    plt.figure(figsize=(12, 8))
    # This is a placeholder since we don't have the exact post-transformed names easily without fitting
    # But we can plot the top N importances
    plt.barh(range(len(importances)), importances)
    plt.title('Feature Importances (Random Forest)')
    plt.savefig(os.path.join(report_dir, 'feature_importance.png'))
    plt.close()
    
    # Save CSV
    importance_df = pd.DataFrame({'importance': importances})
    importance_df.to_csv(os.path.join(report_dir, 'feature_ranking.csv'), index=False)
    
    return importances

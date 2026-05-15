from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from src.utils import get_logger

logger = get_logger('preprocessor')

def get_preprocessing_pipeline(categorical_features, numerical_features):
    """Creates a scikit-learn preprocessing pipeline."""
    logger.info("Building preprocessing pipeline...")
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ]
    )
    
    return preprocessor

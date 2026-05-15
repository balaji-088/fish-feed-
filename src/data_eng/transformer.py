import pandas as pd
from src.utils import get_logger

logger = get_logger('transformer')

class DataTransformer:
    def __init__(self):
        pass
        
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Performs data cleaning and target engineering.
        """
        logger.info("Starting data transformation...")
        
        # Engineering the target: feed_ratio
        # This helps normalize feed quantity across different fish weights
        if 'Feed' in df.columns and 'Fish_Weight' in df.columns:
            df['feed_ratio'] = df['Feed'] / df['Fish_Weight']
            logger.info("Created target feature: feed_ratio")
        
        # Basic cleaning
        df = df.dropna()
        
        return df

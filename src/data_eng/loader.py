import pandas as pd
import os
from src.utils import get_logger

logger = get_logger('data_loader')

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        
    def load_data(self) -> pd.DataFrame:
        """Loads data from CSV file."""
        if not os.path.exists(self.file_path):
            logger.error(f"File not found: {self.file_path}")
            raise FileNotFoundError(f"File not found: {self.file_path}")
            
        logger.info(f"Loading data from {self.file_path}")
        df = pd.read_csv(self.file_path)
        return df

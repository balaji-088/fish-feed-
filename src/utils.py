import logging
import os

def setup_logging(log_file='logs/project.log'):
    """Sets up logging for the project."""
    if not os.path.exists('logs'):
        os.makedirs('logs')
        
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('fish_feed_app')

def get_logger(name):
    return logging.getLogger(name)

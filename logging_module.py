import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)  # Call the actual method
            # Log method exit and result
            logger.info(f"{func.__name__} returned {result}")
            return result
        except Exception as e:
            # Log exceptions if any
            logger.error(f"{func.__name__} raised an exception: {e}")
            raise e
    return wrapper
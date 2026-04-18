import asyncio
from app.services.logger import app_logger as logger

async def retry_async(func, retries: int = 2, delay: int = 1):
    """
    Ssimple retry wrapper for async functions with logging.
    
    Args:
        func: The async function to execute.
        retries: Number of retry attempts.
        delay: Initial delay between retries in seconds.
    """
    last_exception = None
    
    for attempt in range(1, retries + 2):
        try:
            return await func()
        except Exception as e:
            last_exception = e
            if attempt <= retries:
                logger.warning(f"Attempt {attempt} failed: {str(e)}. Retrying in {delay}s...")
                await asyncio.sleep(delay)
            else:
                logger.error(f"All {retries + 1} attempts failed. Final error: {str(e)}")
                raise last_exception
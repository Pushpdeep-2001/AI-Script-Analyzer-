#Retry wrapper
import asyncio

async def retry_async(func, retries=2, delay=1):
    for attempt in range(retries + 1):
        try:
            return await func()
        except Exception as e:
            if attempt == retries:
                raise e
            await asyncio.sleep(delay)
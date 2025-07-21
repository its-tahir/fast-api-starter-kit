import logging
from functools import wraps
from app.core.response import ResponseBuilder
import asyncio

logger = logging.getLogger("instaserve-ai")

def api_response(func):
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            return ResponseBuilder.success(data=result)
        except Exception as exc:
            logger.error(f'[instaserve-ai-debug] Exception in {func.__name__}: {exc}', exc_info=True)
            return ResponseBuilder.error(error=str(exc), message='An error occurred', status_code=500)

    @wraps(func)
    def sync_wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return ResponseBuilder.success(data=result)
        except Exception as exc:
            logger.error(f'[instaserve-ai-debug] Exception in {func.__name__}: {exc}', exc_info=True)
            return ResponseBuilder.error(error=str(exc), message='An error occurred', status_code=500)

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper 
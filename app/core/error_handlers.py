import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from .response import ResponseBuilder
from .exceptions import BusinessLogicError, AuthError
from slowapi.errors import RateLimitExceeded

logger = logging.getLogger("instaserve-ai")

def generic_exception_handler(request: Request, exc: Exception):
    logger.error('Exception caught: %s' % exc, exc_info=True)
    return ResponseBuilder.error(error=str(exc), message='An error occurred', status_code=500)

def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.error('HTTPException caught: %s' % exc.detail, exc_info=True)
    return ResponseBuilder.error(error=exc.detail, message='HTTP error occurred', status_code=exc.status_code)

def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error('Validation error: %s' % exc.errors(), exc_info=True)
    return ResponseBuilder.error(error=exc.errors(), message='Validation error', status_code=422)

def business_logic_error_handler(request: Request, exc: BusinessLogicError):
    logger.error('BusinessLogicError: %s' % exc.message, exc_info=True)
    return ResponseBuilder.error(error=exc.message, message='Business logic error', status_code=exc.status_code)

def auth_error_handler(request: Request, exc: AuthError):
    logger.error('AuthError: %s' % exc.message, exc_info=True)
    return ResponseBuilder.error(error=exc.message, message='Authentication error', status_code=exc.status_code)

def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    logger.error('RateLimitExceeded: %s' % exc.detail, exc_info=True)
    return ResponseBuilder.error(error='Too Many Requests', message='You have exceeded your request rate limit.', status_code=429) 
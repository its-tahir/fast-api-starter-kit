from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.api.v1.endpoints import router as api_router
from app.core.middleware import LoggingMiddleware
from app.core.error_handlers import (
    generic_exception_handler,
    http_exception_handler,
    validation_exception_handler,
    business_logic_error_handler,
    auth_error_handler,
    rate_limit_exceeded_handler,
)
from app.core.exceptions import BusinessLogicError, AuthError
from app.core.config import settings
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

def create_app() -> FastAPI:
    app = FastAPI()
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Rate Limiting
    limiter = Limiter(key_func=get_remote_address, default_limits=[settings.RATE_LIMIT])
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)
    # Register middleware
    app.add_middleware(LoggingMiddleware)
    # Register routers
    app.include_router(api_router)
    # Register exception handlers
    app.add_exception_handler(Exception, generic_exception_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(BusinessLogicError, business_logic_error_handler)
    app.add_exception_handler(AuthError, auth_error_handler)
    return app 
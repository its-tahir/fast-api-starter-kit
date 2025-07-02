import logging
from fastapi import APIRouter
from app.core.response import ResponseBuilder

router = APIRouter()
logger = logging.getLogger("menu-ai")

@router.get('/hello', tags=['Hello'])
def hello_world():
    logger.debug('Hello endpoint called')
    data = {'message': 'Hello, World!'}
    return ResponseBuilder.success(data=data)

@router.get('/hello-error', tags=['Hello'])
def hello_exception():
    logger.debug('Hello exception endpoint called')
    try:
        raise ValueError('This is a raised exception!')
    except Exception as exc:
        return ResponseBuilder.error(error=str(exc), message='Caught an exception in endpoint', status_code=500) 
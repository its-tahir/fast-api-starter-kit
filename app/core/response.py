from fastapi.responses import JSONResponse
from fastapi import Request
import logging

logger = logging.getLogger("menu-ai")

class ResponseBuilder(object):
    @staticmethod
    def success(data=None, message=None):
        logger.debug('Building success response')
        return JSONResponse({
            'success': True,
            'data': data,
            'message': message
        })

    @staticmethod
    def error(error=None, message=None, status_code=400):
        logger.debug('Building error response')
        return JSONResponse({
            'success': False,
            'error': error,
            'message': message
        }, status_code=status_code)

def generic_exception_handler(request: Request, exc: Exception):
    logger.error('Exception caught: %s' % exc, exc_info=True)
    return ResponseBuilder.error(error=str(exc), message='An error occurred', status_code=500) 
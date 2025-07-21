import logging
from fastapi import APIRouter
from app.services.hello_service import HelloService
from app.utils.decorators import api_response

router = APIRouter()
logger = logging.getLogger("instaserve-ai")

@router.get('/hello', tags=['Hello'])
@api_response
def hello_world():
    return HelloService.get_hello_message()

@router.get('/hello-error', tags=['Hello-Error'])
@api_response
def hello_exception():
    return HelloService.raise_hello_exception() 
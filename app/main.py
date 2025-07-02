import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.v1.endpoints.hello import router as hello_router
from app.core.response import generic_exception_handler

logger = logging.getLogger("menu-ai")
logging.basicConfig(level=logging.DEBUG, format='[menu-ai-debug] %(asctime)s %(levelname)s %(message)s')

class Application:
    def __init__(self):
        logger.debug('Initializing FastAPI app')
        self.app = FastAPI()
        self.include_routers()
        self.add_exception_handlers()

    def include_routers(self):
        logger.debug('Including routers')
        self.app.include_router(hello_router)

    def add_exception_handlers(self):
        logger.debug('Adding generic exception handler')
        self.app.add_exception_handler(Exception, generic_exception_handler)

app = Application().app 
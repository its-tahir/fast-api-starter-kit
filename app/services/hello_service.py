import logging

logger = logging.getLogger("instaserve-ai")

class HelloService:
    @staticmethod
    def get_hello_message():
        return {'message': 'Hello, World!'}

    @staticmethod
    def raise_hello_exception():
        raise ValueError('This is a raised exception!') 
import logging

def setup_logger():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s'
    )
    logger = logging.getLogger("instaserve-ai")
    return logger 
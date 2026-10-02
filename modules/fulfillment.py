from utils.logger import logger

class Fulfillment:
    def __init__(self):
        pass

    def run(self, *args, **kwargs):
        logger.info("Fulfillment çalışıyor...")
        return {"status": "success", "module": "fulfillment"}

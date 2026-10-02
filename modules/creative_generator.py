from utils.logger import logger

class CreativeGenerator:
    def __init__(self):
        pass

    def run(self, *args, **kwargs):
        logger.info("Creative Generator çalışıyor...")
        return {"status": "success", "module": "creative_generator"}

from utils.logger import logger

class SupportAgent:
    def __init__(self):
        pass

    def run(self, *args, **kwargs):
        logger.info("Support Agent çalışıyor...")
        return {"status": "success", "module": "support_agent"}

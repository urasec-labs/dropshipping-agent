from utils.logger import logger

class Notifier:
    @staticmethod
    def send_telegram(message: str):
        logger.info(f"Telegram Bildirimi: {message}")

    @staticmethod
    def request_hitl_approval(action_details: str) -> bool:
        logger.warning(f"İnsan Onayı (HITL) Bekleniyor: {action_details}")
        return True

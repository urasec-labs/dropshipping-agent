import requests
from utils.logger import logger

class ResilientScraper:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    def fetch_page(self, url: str) -> str:
        logger.info(f"Sayfa kazınıyor: {url}")
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            logger.error(f"Kazıma hatası: {str(e)}")
        return ""

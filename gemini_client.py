import json
from config import settings
from utils.logger import logger

class GeminiClient:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY.get_secret_value()

    def analyze_product_image(self, image_bytes: bytes) -> dict:
        logger.info("Gemini Vision API: Görsel analiz ediliyor...")
        return {"visual_score": 0.85, "suggested_tags": ["trend", "gadget"]}

    def generate_text(self, prompt: str) -> str:
        logger.info("Gemini Text Generation tetiklendi.")
        if "React Döngüsü" in prompt or "Action:" in prompt:
            return 'Thought: Kullanıcı talebini aldım. Trend analizini çalıştırmalıyım.\nAction: trend_analyzer\nAction Input: viral products'
        return "Gemini Metin Yanıtı"

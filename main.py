import time
from utils.logger import logger
from gemini_client import GeminiClient
from modules.trend_analyzer import TrendAnalyzer
from modules.pricing_engine import PricingEngine
from database.db_manager import init_db

class AutonomousDropshippingAgent:
    def __init__(self):
        self.llm = GeminiClient()
        self.trend = TrendAnalyzer()
        self.pricing = PricingEngine()
        
    def start_loop(self):
        logger.info("Otonom Döngü Başlatıldı...")
        init_db()
        
        # Basit ReAct Mock Çevrimi
        prompt = "React Döngüsü Tetiklendi"
        response = self.llm.generate_text(prompt)
        
        if "Action: trend_analyzer" in response:
            res = self.trend.run("viral products")
            logger.info(f"Ajan Adım Sonucu: {res}")

if __name__ == "__main__":
    agent = AutonomousDropshippingAgent()
    agent.start_loop()

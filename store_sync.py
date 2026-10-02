from utils.logger import logger

class StoreSynchronizer:
    def __init__(self):
        pass

    def push_product(self, product_data: dict) -> bool:
        logger.info(f"Shopify/WooCommerce e-ticaret altyapısına ürün gönderiliyor: {product_data.get('title')}")
        return True

    def fetch_orders(self) -> list:
        logger.info("Mağazadan yeni siparişler çekiliyor...")
        return []

import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr
from typing import Optional

class Settings(BaseSettings):
    GEMINI_API_KEY: SecretStr
    SHOPIFY_API_KEY: Optional[SecretStr] = None
    SHOPIFY_STORE_URL: Optional[str] = None
    
    DATABASE_URL: str = Field(default="sqlite:///./dropshipping.db")
    CHROMA_DB_PATH: str = Field(default="./database/chroma_vector_db")
    
    MIN_PROFIT_MARGIN: float = Field(default=0.30)
    MAX_SHIPPING_DAYS: int = Field(default=15)
    
    TELEGRAM_BOT_TOKEN: Optional[SecretStr] = None
    TELEGRAM_CHAT_ID: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings(GEMINI_API_KEY=SecretStr("mock_key"))

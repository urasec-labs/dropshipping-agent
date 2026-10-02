from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    sku = Column(String, unique=True, index=True)
    source_url = Column(String, nullable=False)
    cogs = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=False)
    stock_status = Column(String, default="IN_STOCK")
    images = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)
    competitors = relationship("CompetitorPrice", back_populates="product", cascade="all, delete-orphan")

class CompetitorPrice(Base):
    __tablename__ = "competitor_prices"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    competitor_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    url = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    product = relationship("Product", back_populates="competitors")

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    shopify_order_id = Column(String, unique=True, index=True)
    customer_info = Column(JSON, nullable=False)
    line_items = Column(JSON, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="PENDING_FULFILLMENT")
    tracking_number = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# product_entity.py

from sqlalchemy import Column, Integer, String, Float
from db.database import Base

class ProductEntity(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "fastapi-crud"}      # CREATE SCHEMA fastapi-crud;

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
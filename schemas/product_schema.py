# product_schema.py

from pydantic import BaseModel

class ProductRequest(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ProductResponse(ProductRequest):
    id: int

    class Config:
        from_attributes = True
# product_schema.py

from datetime import datetime
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator
)


class ProductRequest(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    description: str = Field(
        min_length=5,
        max_length=500
    )

    price: float = Field(
        gt=0
    )

    quantity: int = Field(
        ge=0
    )

    @field_validator("name", "description")
    @classmethod
    def validate_text_fields(cls, value: str):
        value = value.strip()
        if not value:
            raise ValueError(
                "Field cannot be blank"
            )
        return value
    
    @field_validator("price")
    @classmethod
    def validate_price(cls, value: float):
        if round(value, 2) != value:
            raise ValueError(
                "Price can have at most 2 decimal places"
            )
        return value    


class ProductResponse(ProductRequest):

    id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
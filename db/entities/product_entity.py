# product_entity.py

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)
from db.database import Base
from db.mixins.timestamp_mixin import (
    TimestampMixin
)


class ProductEntity(Base, TimestampMixin):
    __tablename__ = "products"
    __table_args__ = {
        "schema": "fastapi-crud"
    }

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    description = Column(
        String(500),
        nullable=False
    )

    price = Column(
        Float,
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False,
        default=0
    )
    
    # created_at = Column(
    #     DateTime(timezone=True),
    #     server_default=func.now()
    # )

    # updated_at = Column(
    #     DateTime(timezone=True),
    #     server_default=func.now(),
    #     onupdate=func.now()
    # )
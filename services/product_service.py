# product_service.py

from sqlalchemy.orm import Session
from repositories import product_repository
from schemas.product_schema import ProductRequest
from exceptions.custom_exceptions import (
    ResourceNotFoundException
)


def get_all_products(db: Session):
    return product_repository.get_all_products(db)


def get_product_by_id(product_id: int, db: Session):
    product = product_repository.get_product_by_id(product_id, db)
    if not product:
        raise ResourceNotFoundException(f"Product with id {product_id} not found")
    return product


def get_products_paginated(page: int, size: int, db: Session):
    return product_repository.get_products_paginated(page, size, db)
    
    
def create_product(product: ProductRequest, db: Session):
    return product_repository.create_product(product, db)


def update_product(product_id: int, product: ProductRequest, db: Session):
    updated_product = product_repository.update_product(product_id, product, db)
    if not updated_product:
        raise ResourceNotFoundException(f"Product with id {product_id} not found")
    return updated_product


def delete_product(product_id: int, db: Session):
    deleted_product = product_repository.delete_product(product_id, db)
    if not deleted_product:
        raise ResourceNotFoundException(f"Product with id {product_id} not found")
    return deleted_product
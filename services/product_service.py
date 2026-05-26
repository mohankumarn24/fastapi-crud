# product_service.py

from sqlalchemy.orm import Session
from repositories import product_repository
from schemas.product_schema import ProductRequest


def get_all_products(db: Session):
    return product_repository.get_all_products(db)


def get_product_by_id(product_id: int, db: Session):
    return product_repository.get_product_by_id(product_id, db)


def create_product(product: ProductRequest, db: Session):
    return product_repository.create_product(product, db)


def update_product(product_id: int, product: ProductRequest, db: Session):
    return product_repository.update_product(product_id, product, db)


def delete_product(product_id: int, db: Session):
    return product_repository.delete_product(product_id, db)
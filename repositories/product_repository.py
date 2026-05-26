# repositories/product_repository.py

from sqlalchemy.orm import Session
from db.entities.product_entity import (
    ProductEntity
)
from repositories.base_repository import (
    BaseRepository
)
from schemas.product_schema import (
    ProductRequest
)


def get_all_products(db: Session):
    return db.query(ProductEntity).all()


def get_product_by_id(product_id: int, db: Session):
    return db.query(ProductEntity).filter(ProductEntity.id == product_id).first()


def get_products_paginated(page: int, size: int, db: Session):
    offset = (page - 1) * size
    return db.query(ProductEntity).offset(offset).limit(size).all()


def create_product(product: ProductRequest, db: Session):
    db_product = ProductEntity(**product.model_dump())
    return BaseRepository.save(db, db_product)


def update_product(product_id: int, product: ProductRequest, db: Session):
    db_product = get_product_by_id(product_id, db)
    if not db_product:
        return None
    
    update_data = product.model_dump()
    for key, value in update_data.items():
        setattr(db_product, key, value)
        
    return BaseRepository.save(db, db_product)


def delete_product(product_id: int, db: Session):
    db_product = get_product_by_id(product_id, db)
    if not db_product:
        return None
    
    try:
        db.delete(db_product)
        db.commit()
        return db_product
    except Exception:
        db.rollback()
        raise
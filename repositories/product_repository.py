# product_repository.py

from sqlalchemy.orm import Session
from db.entities.product_entity import ProductEntity
from schemas.product_schema import ProductRequest


def get_all_products(db: Session):
    return db.query(ProductEntity).all()


def get_product_by_id(product_id: int, db: Session):
    return (
        db.query(ProductEntity)
        .filter(ProductEntity.id == product_id)
        .first()
    )


def create_product(product: ProductRequest, db: Session):
    db_product = ProductEntity(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def update_product(product_id: int, product: ProductRequest, db: Session):
    db_product = get_product_by_id(product_id, db)

    if not db_product:
        return None

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.quantity = product.quantity

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(product_id: int, db: Session):
    db_product = get_product_by_id(product_id, db)

    if not db_product:
        return None

    db.delete(db_product)
    db.commit()

    return db_product
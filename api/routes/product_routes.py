# product_routes.py

from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from dependencies.database_dependency import get_db
from services import product_service
from schemas.product_schema import (
    ProductRequest,
    ProductResponse
)
import logging

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"]
)


@router.get("/", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    logger.info("Fetching all products")
    return product_service.get_all_products(db)


@router.get("/paginated", response_model=list[ProductResponse])
def get_products_paginated(
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),
    db: Session = Depends(get_db)
):

    logger.info(
        f"Fetching paginated products "
        f"page={page}, size={size}"
    )
    return product_service.get_products_paginated(page, size, db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching product with id {product_id}")
    return product_service.get_product_by_id(product_id, db)
    
    
@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductRequest, db: Session = Depends(get_db)):
    logger.info(f"Creating product: {product.name}")
    return product_service.create_product(product, db)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductRequest, db: Session = Depends(get_db)):
    logger.info(f"Updating product with id {product_id}")
    return product_service.update_product( product_id, product, db)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting product with id {product_id}")
    product_service.delete_product(product_id, db)

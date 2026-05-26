# product_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies.database_dependency import get_db
from schemas.product_schema import (
    ProductRequest,
    ProductResponse
)
from services import product_service


router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"]
)


@router.get("/", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    return product_service.get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """
    Get product by ID
    Raises 404 if product not found
    """
    product = product_service.get_product_by_id(product_id, db)

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    return product


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductRequest, db: Session = Depends(get_db)):
    return product_service.create_product(product, db)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductRequest, db: Session = Depends(get_db)):
    updated_product = product_service.update_product(product_id, product, db)

    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return updated_product


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = product_service.delete_product(product_id, db)

    if not deleted_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    return {"message": "Product deleted successfully"}
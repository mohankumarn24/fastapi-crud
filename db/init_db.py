# init_db.py

from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.entities.product_entity import ProductEntity


def seed_database():
    db: Session = SessionLocal()
    existing_products = db.query(ProductEntity).count()

    if existing_products == 0:

        products = [
            ProductEntity(name="Phone", description="A smartphone", price=699.99, quantity=50),
            ProductEntity(name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
            ProductEntity(name="Pen", description="Blue ink pen", price=1.99, quantity=100),
            ProductEntity(name="Table", description="Wooden table", price=199.99, quantity=20),
        ]

        db.add_all(products)
        db.commit()

        print("Database seeded successfully")

    db.close()
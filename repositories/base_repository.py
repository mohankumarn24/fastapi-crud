# repositories/base_repository.py

from sqlalchemy.orm import Session


class BaseRepository:
    
    @staticmethod
    def save(db: Session, entity):
        try:
            db.add(entity)
            db.commit()
            db.refresh(entity)
            return entity
        except Exception:
            db.rollback()
            raise
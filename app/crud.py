from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.name = user.name
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {"message": f"User with ID {user_id} deleted successfully"}
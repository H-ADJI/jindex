'''
File: crud.py
File Created: Wednesday, 1st February 2023 12:56:28 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from sqlalchemy.orm import Session
from app.database import models
from .models import Keyword
from app.api.schemas import KeywordCreate
from pydantic import BaseModel
from .db import Base


def get_by_id(model: Base, id: int, db_session: Session):
    return db_session.query(model).filter(model.id == id).first()


def delete_by_id(model: Base, id: int, db_session: Session):
    to_delete = db_session.query(model).filter(model.id == id).first()
    if to_delete:
        db_session.delete(instance=to_delete)
        db_session.commit()


def read_full_table(model: Base, db_session: Session):
    return db_session.query(model).all()


def create_table_entry(data: BaseModel, model: Base, db_session: Session):
    db_data = model(**data.dict())
    db_session.add(db_data)
    db_session.commit()
    db_session.refresh(db_data)
    return db_data

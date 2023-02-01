'''
File: crud.py
File Created: Wednesday, 1st February 2023 12:56:28 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from sqlalchemy.orm import Session
from app.database import models


def get_keywords(db_session: Session):
    return db_session.query(models.Keyword).all()

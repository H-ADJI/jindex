'''
File: keywords.py
File Created: Wednesday, 1st February 2023 7:05:18 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db_session
from app.database.crud import create_table_entry, read_full_table, get_by_id, delete_by_id
from app.database.models import Keyword
from app.api.schemas import KeywordRead, KeywordCreate
router = APIRouter(prefix="/keyword")


@router.post(path="/new")
async def add_keyword(location: KeywordCreate, session: Session = Depends(get_db_session)) -> KeywordRead:
    db_location = create_table_entry(
        location, model=KeywordCreate, db_session=session)
    return db_location


@router.get(path="/all")
async def get_all_keywords(session=Depends(get_db_session)) -> list[KeywordRead]:
    return read_full_table(model=KeywordCreate, db_session=session)


@router.post(path="/{id}")
async def get_keyword(id: int, session: Session = Depends(get_db_session)) -> Optional[KeywordRead]:
    return get_by_id(model=KeywordCreate, id=id, db_session=session)


@router.delete(path="/{id}")
async def delete_keyword(id: int, session: Session = Depends(get_db_session)):
    delete_by_id(model=KeywordCreate, id=id, db_session=session)

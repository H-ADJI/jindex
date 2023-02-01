'''
File: search_params.py
File Created: Tuesday, 31st January 2023 10:15:37 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from fastapi import APIRouter, Depends
from app.database.db import get_db_session
from app.database.crud import get_keywords
router = APIRouter(prefix="/query")


@router.post(path="/new")
async def add_location():
    pass


@router.get(path="/all")
async def get_all_locations(session=Depends(get_db_session)):

    return get_keywords(db_session=session)


@router.post(path="/{id}")
async def get_location():
    pass


@router.delete(path="/{id}")
async def delete_location():
    pass

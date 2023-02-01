'''
File: search_params.py
File Created: Tuesday, 31st January 2023 10:15:37 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db_session
from app.database.crud import create_table_entry, read_full_table, get_by_id, delete_by_id
from app.database.models import Location
from app.api.schemas import LocationCreate, LocationRead
router = APIRouter(prefix="/location")


@router.post(path="/new")
async def add_location(location: LocationCreate, session: Session = Depends(get_db_session)) -> LocationRead:
    db_location = create_table_entry(
        location, model=Location, db_session=session)
    return db_location


@router.get(path="/all")
async def get_all_locations(session=Depends(get_db_session)) -> list[LocationRead]:
    return read_full_table(model=Location, db_session=session)


@router.post(path="/{id}")
async def get_location(id: int, session: Session = Depends(get_db_session)) -> Optional[LocationRead]:
    return get_by_id(model=Location, id=id, db_session=session)


@router.delete(path="/{id}")
async def delete_location(id: int, session: Session = Depends(get_db_session)):
    delete_by_id(model=Location, id=id, db_session=session)

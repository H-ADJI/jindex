'''
File: jobs.py
File Created: Wednesday, 1st February 2023 8:22:58 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from typing import Optional
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database.db import get_db_session
from app.database.crud import create_table_entry, read_full_table, get_by_id, delete_by_id
from app.database.models import Keyword
from app.api.schemas import SearchParams
router = APIRouter(prefix="/job")


@router.post(path="/collect")
async def get_keyword(search_params: SearchParams, bg_task: BackgroundTasks, session: Session = Depends(get_db_session)):
    print(search_params.dict())

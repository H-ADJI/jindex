'''
File: schemas.py
File Created: Wednesday, 1st February 2023 12:41:17 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from pydantic import BaseModel


class KeywordBase(BaseModel):
    keyword: str
    

class LocationBase(BaseModel):
    location: str


class JobBase(BaseModel):
    title: str
    linkedin_id: str
    title:  str
    url: str
    location: str
    date: str
    company: str
    company_url: str

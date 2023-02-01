'''
File: schemas.py
File Created: Wednesday, 1st February 2023 12:41:17 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from pydantic import BaseModel, Field


class KeywordBase(BaseModel):
    keyword: str

    class Config:
        orm_mode = True


class KeywordCreate(KeywordBase):
    pass


class KeywordRead(KeywordBase):
    id: int


class LocationBase(BaseModel):
    location: str

    class Config:
        orm_mode = True


class LocationCreate(LocationBase):
    location: str = Field(max_length=20)


class LocationRead(LocationBase):
    id: int


class JobBase(BaseModel):
    title: str
    linkedin_id: str
    title:  str
    url: str
    location: str
    date: str
    company: str
    company_url: str


class SearchParams(BaseModel):
    keywords: list[str]
    locations: list[str]

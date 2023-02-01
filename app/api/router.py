'''
File: router.py
File Created: Tuesday, 31st January 2023 10:02:33 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from fastapi import APIRouter
from .routes import locations, keywords, jobs

api_router = APIRouter(prefix="/api")

api_router.include_router(router=locations.router, tags=[
                          "locations"])
api_router.include_router(router=keywords.router, tags=[
                          "search terms"])
api_router.include_router(router=jobs.router, tags=[
                          "jobs crawling and manipulation"])
# router for auth
# router for similarity
# router for search index and filtering
# router for  crud on job analytics

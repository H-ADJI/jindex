'''
File: router.py
File Created: Tuesday, 31st January 2023 10:02:33 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from fastapi import APIRouter
from .routes import query

api_router = APIRouter(prefix="/api")

api_router.include_router(router=query.router, tags=[
                          "locations and search terms"])
# router for auth
# router for tags and keywords
# router for similarity
# router for search index and filtering
# router for  crud on job analytics

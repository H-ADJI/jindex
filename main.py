'''
File: main.py
File Created: Tuesday, 31st January 2023 10:02:15 pm
Author: KHALIL HADJI 
-----
Copyright:  KHALIL HADJI 2023
'''
from fastapi import FastAPI
import uvicorn
from app.api.router import api_router

#  startup / shutdown events
app = FastAPI(title="jIndex_api", version="0.0.0")
app.include_router(router=api_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8000, reload=True)

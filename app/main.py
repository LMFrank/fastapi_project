# -*- coding: utf-8 -*-
from fastapi import FastAPI
import uvicorn
from app.configs import database, API_PREFIX
from app.api.api_1_0.api import router

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome to FastAPI CRUD."}

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(router, prefix=API_PREFIX, tags=["books"])


if __name__ == '__main__':
    uvicorn.run(app="main:app", host="192.168.148.129", port=8000, reload=True, debug=True)
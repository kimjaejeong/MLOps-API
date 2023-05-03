# from pandas.core.frame import DataFrame
from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
async def root():
    raise HTTPException(status_code=500, detail="Internal Server Error")

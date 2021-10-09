from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

db = []

class City(BaseModel):
    name : str
    timezone : str

@app.get("/")
def root():
    return {"Hello" : "재정!"}

@app.get("/cities")
def get_cities():
    results = []
    for city in db:
        strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        results.append({'name' : city['name'], 'timezone' : city['timezone'], 'current_time' : cur_time})

    return results

@app.post("/cities")
def create_city(city : City):
    db.append(city.dict())
    return db[-1]

@app.get("/cities/{city_id}")
def get_city(city_id : int):
    city = db[city_id - 1]
    strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
    r = requests.get(strs)
    cur_time = r.json()['datetime']
    return {'name' : city['name'], 'timezone' : city['timezone'], 'current_time' : cur_time}

@app.delete("/cities/{city_id}")
def delete_city(city_id : int):
    db.pop(city_id - 1)
    return {}

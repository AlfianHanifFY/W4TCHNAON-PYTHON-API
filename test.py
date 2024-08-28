import json
from fastapi import FastAPI
import numpy as np
app = FastAPI()


@app.get("/data")
async def get_data(data):
    data = json.loads(data)
    name = []
    for user in data:
        name.append(user["name"])
    return {"data": name,
            "message": f"success"}
    
@app.get("/data/recommendation-movie")
async def get_data(movies, movie_id):

    return { "message" : "result" }
    
    
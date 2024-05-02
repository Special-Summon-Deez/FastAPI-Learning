import os
from fastapi import FastAPI
from enum import Enum

from motor import motor_asyncio

#app is the instance of our FastAPI.
app = FastAPI(
    title = "YuGiOh Simple DB",
    description = "Intended to display simple information about yugioh cards within database"
)

client = motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.card_database
collection = db.card_collection

class setName(str, Enum):
    LOB = "Legend of Blue-Eyes"
    MRD = "Metal Raiders"
    SECE = "Secrets of Eternity"


@app.get("/")
async def root():
    return {"message": "This is a test message"}

@app.get("/cards/{card_id}")
async def read_item(card_id : str):
    return{"card_id" : {card_id}}

@app.get("/sets/{setName}")
async def get_set(set_name : setName):
    if set_name is setName.LOB:
        return {"set_name": set_name, "message" : "The first set of the TCG"}
    
    if set_name is setName.MRD:
        return{"set_name" : set_name, "message" : "The second set of the TCG"}
    
    return{"set_name" : set_name, "message" : "Some zoomer stuff right here man, idk"}
import os
from fastapi import FastAPI

app = FastAPI(
    title = "YuGiOh Simple DB",
    description = "Intended to display simple information about yugioh cards within database"
)


@app.get("/")
async def root():
    return {"message": "This is a test message"}
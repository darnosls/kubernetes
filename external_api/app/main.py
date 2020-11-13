import httpx
import os

from fastapi import FastAPI
from loguru import logger


app = FastAPI()


@app.get("/")
async def root():
    logger.info("Starts external api")

    url = "http://localhost:8000/" if os.getenv("SERVICE_URL") == None else f"{os.getenv('SERVICE_URL')}:8001"



    logger.info("Starts call internal api url={}", url)
    res = await httpx.get(url)
    logger.info("Ends call internal api url={}", url)

    internal_res = res.json()

    logger.info("Ends external api")
    return {
        "message": "api externa",
        "internal_message": f"{internal_res.get('message')} ..."
        }

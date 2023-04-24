from fastapi import FastAPI, Depends
from src.config import get_settings, Settings

app = FastAPI()


@app.get("/")
async def task(settings: Settings = Depends(get_settings)):
    """This is the initial task

    Returns:
        [dict] -- [This is the initial task]"""

    return {"task": "Initial task"}

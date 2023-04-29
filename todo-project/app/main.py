from fastapi import FastAPI, Depends
from app.routes.task import router as TaskRouter

app = FastAPI()

app.include_router(TaskRouter, tags=["Task"], prefix="/task")


@app.get("/", tags=["Root"])
async def task():
    """This is the initial task

    Returns:
        [dict] -- [This is the initial task]"""

    return {"task": "Initial task"}

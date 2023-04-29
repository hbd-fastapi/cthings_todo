from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.database import (
    add_task,
    delete_task,
    retrieve_task,
    retrieve_tasks,
    update_task,
)

from app.models.task import (
    ErrorResponseModel,
    ResponseModel,
    TaskSchema,
    UpdateTaskModel,
)

router = APIRouter()


@router.post("/", response_description="Task data added into the database")
async def add_task_data(task: TaskSchema = Body(...)):
    task = jsonable_encoder(task)
    new_task = await add_task(task)
    return ResponseModel(new_task, "Student added successfully.")

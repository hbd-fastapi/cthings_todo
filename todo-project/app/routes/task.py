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

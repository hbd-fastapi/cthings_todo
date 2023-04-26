from typing import Optional

from pydantic import BaseModel


class TaskSchema(BaseModel):
    title: str = None
    description: Optional[str] = None
    status: bool = False

    class Config:
        schema_extra = {
            "example": {
                "title": "Create a todo app with FastAPI",
                "description": "You need to finish the task to get the job.",
                "status": True,
            }
        }


class UpdateTaskModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "title": "Create a todo app with FastAPI",
                "description": "You need to finish the task to get the job.",
                "status": True,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

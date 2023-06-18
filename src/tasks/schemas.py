from typing import Optional, TypeAlias, List
from pydantic import BaseModel, Field


class Task(BaseModel):
    title: Optional[str] = Field(None, example="My task")
    user_id: int = Field(..., example=1)

    class config:
        orm_mode = True


class TaskResponse(Task):
    id: int = Field(..., example=1)


class CreateTaskRequest(Task):
    pass


class CreateTaskResponse(TaskResponse):
    pass


class GetTasksResponse(BaseModel):
    data: List[TaskResponse] = Field([], example="My task")

    class config:
        orm_mode = True


class GetTaskResponse(TaskResponse):
    pass

from typing import Optional, TypeAlias, List
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="My task")
    user_id: int = Field(..., example=1)

    class config:
        orm_mode = True


class Task(TaskBase):
    id: int = Field(..., example=1)


CreateTaskRequest: TypeAlias = TaskBase
CreateTaskResponse: TypeAlias = Task
GetTasksResponse: TypeAlias = List[Task]
UpdateTaskRequest: TypeAlias = TaskBase
UpdateTaskResponse: TypeAlias = Task

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from . import service
from ..database import get_db
from schemas import CreateTaskRequest, GetTasksResponse

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.post("/tasks", response_model=CreateTaskRequest)
async def create_task(
    body: CreateTaskRequest,
    db: AsyncSession = Depends(get_db),
):
    return service.create_task(db, body)


@router.get("/tasks", response_model=GetTasksResponse)
async def get_tasks(db: AsyncSession = Depends(get_db)):
    return await service.get_tasks(db)

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.tasks import service, schemas
from src.database import get_db

router = APIRouter()


@router.post("/tasks", response_model=schemas.CreateTaskResponse)
async def create_task(
    body: schemas.CreateTaskRequest,
    db: AsyncSession = Depends(get_db),
):
    return await service.create_task(db, body)


@router.get("/tasks", response_model=schemas.GetTasksResponse)
async def get_tasks(db: AsyncSession = Depends(get_db)):
    return await service.get_tasks(db)


@router.get("/tasks/{task_id}", response_model=schemas.GetTaskResponse)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_task(db, task_id)

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from tasks import service, schemas
from database import get_db

router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.post("/tasks", response_model=schemas.CreateTaskRequest)
async def create_task(
    body: schemas.CreateTaskRequest,
    db: AsyncSession = Depends(get_db),
):
    return service.create_task(db, body)


@router.get("/tasks", response_model=schemas.GetTasksResponse)
async def get_tasks(db: AsyncSession = Depends(get_db)):
    return await service.get_tasks(db)

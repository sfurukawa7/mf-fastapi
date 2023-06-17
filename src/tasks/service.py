from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Task
from schemas import CreateTaskRequest, UpdateTaskRequest


async def create_task(db: AsyncSession, body: CreateTaskRequest):
    task = Task(**body.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks(db: AsyncSession):
    result = await db.execute(
        select(
            Task.id,
            Task.title,
        )
    )
    return result.all()


async def get_task(db: AsyncSession, id: int):
    result = await db.execute(select(Task).filter(Task.id == id))
    task = result.first()
    return task[0] if task else None


async def update_task(db: AsyncSession, id: int, body: UpdateTaskRequest):
    task = await get_task(db, id)
    if not task:
        return None
    for field, value in vars(body):
        setattr(task, field, value)
    await db.commit()
    await db.refresh(task)
    return task

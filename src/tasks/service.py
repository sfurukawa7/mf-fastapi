from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from tasks import models, schemas


async def create_task(db: AsyncSession, body: schemas.CreateTaskRequest):
    task = models.Task(**body.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks(db: AsyncSession):
    result = await db.execute(select(models.Task))
    return result.all()


async def get_task(db: AsyncSession, id: int):
    result = await db.execute(select(models.Task).filter(models.Task.id == id))
    task = result.first()
    return task[0] if task else None


async def update_task(db: AsyncSession, id: int, body: schemas.UpdateTaskRequest):
    task = await get_task(db, id)
    if not task:
        return None
    for field, value in vars(body):
        setattr(task, field, value)
    await db.commit()
    await db.refresh(task)
    return task

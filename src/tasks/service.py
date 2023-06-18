from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from src.tasks import models, schemas
from src.utils import row_to_dict


async def create_task(db: AsyncSession, body: schemas.CreateTaskRequest):
    insert_query = insert(models.Task).values(
        {"title": body.title, "user_id": body.user_id}
    )

    result = await db.execute(insert_query)
    await db.commit()
    return {**body.dict(), "id": result.inserted_primary_key[0]}


async def get_tasks(db: AsyncSession):
    result = await db.scalars(select(models.Task))
    return {"data": [row_to_dict(x) for x in result]}


async def get_task(db: AsyncSession, id: int):
    result = await db.scalar(select(models.Task).filter(models.Task.id == id))
    task = row_to_dict(result)
    return task if task else None


# async def update_task(db: AsyncSession, id: int, body: schemas.UpdateTaskRequest):
#     task = await get_task(db, id)
#     if not task:
#         return None
#     for field, value in vars(body):
#         setattr(task, field, value)
#     await db.commit()
#     await db.refresh(task)
#     return task

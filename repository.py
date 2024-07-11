from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import TaskAdd, Task


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            tasks_models = result.scalars().all()
            tasks_schemas = [task.model_validate() for task in tasks_models]
            return tasks_schemas

from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, exercises

router = APIRouter(
    prefix='/exercises',
    tags=['exercises']
)


class Exercise(BaseModel):
    name: str
    muscle_type: int
    level: int


@router.post('/new')
async def register_exercises(exercise: Exercise):
    last_record_id = await database.execute(exercises.insert().values(**exercise.dict()))
    return {**exercise.dict(), 'id': last_record_id}


@router.get('/')
async def get_exercises():
  return await database.fetch_all(exercises.select())
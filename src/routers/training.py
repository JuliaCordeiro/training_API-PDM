from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, training

router = APIRouter(
    prefix='/training',
    tags=['training']
)


class Training(BaseModel):
    training_id: int
    exercises_id: int
    muscle_group: int


@router.post('/new')
async def register_training(traine: Training):
    last_record_id = await database.execute(training.insert().values(**traine.dict()))
    return {**traine.dict(), 'id': last_record_id}


@router.get('/')
async def get_training():
  return await database.fetch_all(training.select())

# TODO: Change the column exercises_id item_type to Array or similar in SQLite
from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, training

router = APIRouter(
    prefix='/training',
    tags=['training']
)


class Training(BaseModel):
    protocol_id: int
    muscle_group: int


@router.post('/new')
async def register_training(traine: Training):
    last_record_id = await database.execute(training.insert().values(**traine.dict()))
    return {**traine.dict(), 'id': last_record_id}


@router.get('/')
async def get_training():
  return await database.fetch_all(training.select())


@router.get('/single')
async def get_one_training(training_id: int):
  return await database.fetch_one(training.select().where( training.columns.id == training_id))

# TODO: Change the column exercises_id item_type to Array or similar in SQLite
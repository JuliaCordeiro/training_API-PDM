from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, users

router = APIRouter(
    prefix='/users',
    tags=['users']
)


class User(BaseModel):
    full_name: str
    activity_leveling: int
    gender: int
    weight: float
    height: float
    username: str
    password:str

@router.post('/new')
async def register_users(user: User):
    last_record_id = await database.execute(users.insert().values(**user.dict()))
    return {**user.dict(), 'id': last_record_id}


@router.get('/')
async def get_users():
  return await database.fetch_all(users.select())
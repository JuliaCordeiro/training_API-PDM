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


@router.get('/single')
async def get_one_users(user_id: int):
    return await database.fetch_one(users.select().where( users.columns.id == user_id))


@router.get('/user')
async def get_one_users(username: str, password: str):
    return await database.fetch_one(users.select().where( users.columns.username == username and users.columns.password == password))

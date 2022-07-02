from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, relationships

router = APIRouter(
    prefix='/relationships',
    tags=['relationships']
)


class Relationship(BaseModel):
    exercise_id: int
    training_id: int


@router.post('/new')
async def register_relationship(relation: Relationship):
    last_record_id = await database.execute(relationships.insert().values(**relation.dict()))
    return {**relation.dict(), 'id': last_record_id}


@router.get('/')
async def get_relationship():
  return await database.fetch_all(relationships.select())


@router.get('/single')
async def get_one_relationship(relationship_id: int):
  return await database.fetch_one(relationships.select().where( relationships.columns.id == relationship_id))
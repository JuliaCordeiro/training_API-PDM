from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, relationships, exercises

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
    return await database.fetch_one(relationships.select().where( relationships.columns.id == relationship_id ))


@router.get('/group')
async def get_relationship_by_training(training_id: int):
    return await database.fetch_all(relationships.select().where( relationships.columns.training_id == training_id ))


@router.get('/exercises')
async def get_exercises_by_training(training_id: int):
    relationships_by_training = await database.fetch_all(relationships.select().where( relationships.columns.training_id == training_id ))
    training_exercises = []
    for exercise_id in relationships_by_training:
        training_exercises.append(await database.fetch_one(exercises.select().where( exercises.columns.id == exercise_id[1])))
    return training_exercises

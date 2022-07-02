from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, protocol

router = APIRouter(
    prefix='/protocol',
    tags=['protocol']
)


class Protocol(BaseModel):
    user_id: int


@router.post('/new')
async def register_protocol(prot: Protocol):
    last_record_id = await database.execute(protocol.insert().values(**prot.dict()))
    return {**prot.dict(), 'id': last_record_id}


@router.get('/')
async def get_protocol():
  return await database.fetch_all(protocol.select())


@router.get('/single')
async def get_one_protocol(protocol_id: int):
  return await database.fetch_one(protocol.select().where( protocol.columns.id == protocol_id))

# TODO: Change the column division item_type to Array or similar in SQLite
from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, protocol

router = APIRouter(
    prefix='/protocol',
    tags=['protocol']
)


class Protocol(BaseModel):
    user_id: int
    division: int


@router.post('/new')
async def register_protocol(prot: Protocol):
    last_record_id = await database.execute(protocol.insert().values(**prot.dict()))
    return {**prot.dict(), 'id': last_record_id}


@router.get('/')
async def get_protocol():
  return await database.fetch_all(protocol.select())

# TODO: Change the column division item_type to Array or similar in SQLite
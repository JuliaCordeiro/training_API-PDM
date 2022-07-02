from fastapi import FastAPI
from src.constants import TAGS_METADATA
from src.database.database import database
from src.routers import exercises

app = FastAPI(
    title='TrainingAPI',
    description='An API to perform database operations of a Training App',
    openapi_tags=TAGS_METADATA
)

app.include_router(exercises.router)

@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/ping')
async def ping():
    return {'message': 'ping'}
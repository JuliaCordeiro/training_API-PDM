from fastapi import FastAPI
from src.constants import TAGS_METADATA
from src.database.database import database
from src.routers import exercises, users, protocol, training, relationships

app = FastAPI(
    title='TrainingAPI',
    description='An API to perform database operations of a Training App',
    openapi_tags=TAGS_METADATA
)

app.include_router(exercises.router)
app.include_router(users.router)
app.include_router(protocol.router)
app.include_router(training.router)
app.include_router(relationships.router)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/ping')
async def ping():
    return {'message': 'ping'}
import sqlalchemy
from databases import Database
from src.constants import DATABASE_URL

database = Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('full_name', sqlalchemy.String),
    sqlalchemy.Column('activity_leveling', sqlalchemy.Integer),
    sqlalchemy.Column('gender', sqlalchemy.Integer),
    sqlalchemy.Column('weight', sqlalchemy.Float),
    sqlalchemy.Column('height', sqlalchemy.Integer),
    sqlalchemy.Column('username', sqlalchemy.String),
    sqlalchemy.Column('password', sqlalchemy.String)
)

exercises = sqlalchemy.Table(
    'exercises',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('muscle_type', sqlalchemy.Integer),
    sqlalchemy.Column('level', sqlalchemy.Integer)
)

protocol = sqlalchemy.Table(
    'protocol',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer)
)

training = sqlalchemy.Table(
    'training',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('protocol_id', sqlalchemy.Integer),
    sqlalchemy.Column('muscle_group', sqlalchemy.Integer)
)

relationships = sqlalchemy.Table(
    'relationships',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('exercise_id', sqlalchemy.Integer),
    sqlalchemy.Column('training_id', sqlalchemy.Integer)
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

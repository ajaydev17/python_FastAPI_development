import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DEV_DATABASE_URL = os.getenv('DEV_DATABASE_URL')

if not DEV_DATABASE_URL:
    raise ValueError('Missing required environment variable DEV_DATABASE_URL')

engine = create_engine(DEV_DATABASE_URL)
local_session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()


# get the db session
def get_db_session():
    db = local_session()

    try:
        yield db
    finally:
        db.close()

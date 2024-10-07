import pytest
from tests.utils.docker_utils import start_database_container
from sqlalchemy import create_engine
from .utils import database_utils
from dotenv import load_dotenv
import os

load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def db_session():
    container = start_database_container()

    test_database_url = os.environ.get('TEST_DATABASE_URL')
    engine = create_engine(test_database_url)

    with engine.begin() as connection:
        database_utils.migrate_to_db('migrations', 'alembic.ini', connection)

    # stopping the container once test is done
    # container.stop()
    # container.remove()

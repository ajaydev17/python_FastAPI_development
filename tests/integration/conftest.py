import pytest

from app.db_connection import get_db_session
from tests.utils.docker_utils import start_database_container
from sqlalchemy import create_engine
from tests.utils import database_utils
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.main import app
import os

load_dotenv()


# @pytest.fixture(scope='session', autouse=True)
@pytest.fixture(scope='function')
def db_session_integration():
    container = start_database_container()

    test_database_url = os.environ.get('TEST_DATABASE_URL')
    engine = create_engine(test_database_url)

    with engine.begin() as connection:
        database_utils.migrate_to_db('migrations', 'alembic.ini', connection)

    local_session = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    db = local_session()

    try:
        yield db
    finally:
        db.close()

    # stopping the container once test is done
    container.stop()
    container.remove()

    engine.dispose()


@pytest.fixture()
def override_get_db_session(db_session_integration):
    def override():
        return db_session_integration

    app.dependency_overrides[get_db_session()] = override


@pytest.fixture(scope='function')
def client():
    with TestClient(app) as _client:
        yield _client

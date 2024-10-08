import pytest
from sqlalchemy import inspect
from ..fixtures import db_session


@pytest.fixture(scope='function')
def db_inspector(db_session):
    return inspect(db_session().bind)

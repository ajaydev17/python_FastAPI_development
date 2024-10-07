import pytest
from tests.fixtures import db_session


def test_true(db_session):
    assert True

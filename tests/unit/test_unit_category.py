import pytest
from pydantic import ValidationError
from app.schemas.category_schema import CategoryCreate
from tests.factories.models_factory import get_random_category_dict


def mock_output(return_value=None):
    return lambda *args, **kwargs: return_value


"""
- [ ] Test category schema valid and invalid data 
"""


def test_unit_schema_category_validation():
    valid_data = {
        'name': 'test-category',
        'slug': 'test-slug'
    }

    category = CategoryCreate(**valid_data)
    assert category.name == 'test-category'
    assert category.is_active is False
    assert category.level == 100
    assert category.parent_id is None

    invalid_data = {
        'name': 'test-slug'
    }

    with pytest.raises(ValidationError):
        CategoryCreate(**invalid_data)


"""
- [ ] Test POST new category successfully
"""


def test_unit_create_new_category_successful(client, monkeypatch):
    category = get_random_category_dict()

    monkeypatch.setattr('sqlalchemy.orm.Query.first', mock_output())
    monkeypatch.setattr('sqlalchemy.orm.Session.commit', mock_output())
    monkeypatch.setattr('sqlalchemy.orm.Session.refresh', mock_output())

    body = category.copy()
    body.pop('id')

    response = client.post('api/category', json=body)

    assert response.status_code == 201
    assert response.json() == category


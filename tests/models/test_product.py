"""
## Table and Column Validation
"""
from .fixtures import db_inspector
from sqlalchemy import Integer, String, Boolean, Text, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""


def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table('product')


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""


def test_model_structure_column_data_type(db_inspector):
    table = 'product'
    columns = {columns['name']: columns for columns in db_inspector.get_columns(table)}

    assert isinstance(columns['id']['type'], Integer)
    assert isinstance(columns['pid']['type'], UUID)
    assert isinstance(columns['name']['type'], String)
    assert isinstance(columns['slug']['type'], String)
    assert isinstance(columns['description']['type'], Text)
    assert isinstance(columns['is_digital']['type'], Boolean)
    assert isinstance(columns['created_at']['type'], DateTime)
    assert isinstance(columns['updated_at']['type'], DateTime)
    assert isinstance(columns['is_active']['type'], Boolean)
    assert isinstance(columns['stock_status']['type'], Enum)
    assert isinstance(columns['category_id']['type'], Integer)
    assert isinstance(columns['seasonal_event']['type'], Integer)


"""
- [ ] Verify nullable or not nullable fields
"""


def test_model_structure_nullable_constraints(db_inspector):
    table = 'product'
    columns = db_inspector.get_columns(table)

    expected_nulls = {
        'id': False,
        'pid': False,
        'name': False,
        'slug': False,
        'description': True,
        'is_digital': False,
        'created_at': False,
        'updated_at': False,
        'is_active': False,
        'stock_status': False,
        'category_id': False,
        'seasonal_event': True
    }

    for column in columns:
        column_name = column['name']
        assert column['nullable'] == expected_nulls.get(
            column_name), f"column '{column_name}' is not nullable as expected."


"""
- [ ] Test columns with specific constraints to ensure they are accurately defined.
"""


def test_model_structure_column_constraints(db_inspector):
    table = 'product'
    constraints = db_inspector.get_check_constraints(table)

    assert any(constraint['name'] == 'product_name_length_check' for constraint in constraints)
    assert any(constraint['name'] == 'product_slug_length_check' for constraint in constraints)


"""
- [ ] Verify the correctness of default values for relevant columns.
"""


def test_model_structure_default_values(db_inspector):
    table = 'product'
    columns = {columns['name']: columns for columns in db_inspector.get_columns(table)}

    assert columns['is_digital']['default'] == 'false'
    assert columns['is_active']['default'] == 'false'
    assert columns['stock_status']['default'] == "'oos'::status_enum"


"""
- [ ] Ensure that column lengths align with defined requirements.
"""


def test_model_structure_column_lengths(db_inspector):
    table = 'product'
    columns = {columns['name']: columns for columns in db_inspector.get_columns(table)}

    assert columns['name']['type'].length == 200
    assert columns['slug']['type'].length == 220


"""
- [ ]  Validate the enforcement of unique constraints for columns requiring unique values.
"""


def test_model_structure_unique_constraints(db_inspector):
    table = 'product'
    constraints = db_inspector.get_unique_constraints(table)

    assert any(constraint['name'] == 'uq_category_name_level' for constraint in constraints)
    assert any(constraint['name'] == 'uq_category_slug' for constraint in constraints)

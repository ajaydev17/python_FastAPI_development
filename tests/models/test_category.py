"""
## Table and Column Validation
"""
from .fixtures import db_inspector
from sqlalchemy import Integer, String, Boolean

"""
- [ ] Confirm the presence of all required tables within the database schema.
"""


def test_model_structure_table_exists(db_inspector):
    assert db_inspector.has_table('category')


"""
- [ ] Validate the existence of expected columns in each table, ensuring correct data types.
"""


def test_model_structure_column_data_type(db_inspector):
    table = 'category'
    columns = {columns['name']: columns for columns in db_inspector.get_columns(table)}

    assert isinstance(columns['id']['type'], Integer)
    assert isinstance(columns['name']['type'], String)
    assert isinstance(columns['slug']['type'], String)
    assert isinstance(columns['is_active']['type'], Boolean)
    assert isinstance(columns['level']['type'], Integer)
    assert isinstance(columns['parent_id']['type'], Integer)


"""
- [ ] Verify nullable or not nullable fields
"""


def test_model_structure_nullable_constraints(db_inspector):
    table = 'category'
    columns = db_inspector.get_columns(table)

    expected_nulls = {
        'id': False,
        'name': False,
        'slug': False,
        'is_active': False,
        'level': False,
        'parent_id': True
    }

    for column in columns:
        column_name = column['name']
        assert column['nullable'] == expected_nulls.get(column_name), f"column '{column_name}' is not nullable as expected."


"""
- [ ] Test columns with specific constraints to ensure they are accurately defined.
"""

"""
- [ ] Verify the correctness of default values for relevant columns.
"""

"""
- [ ] Ensure that column lengths align with defined requirements.
"""

"""
- [ ]  Validate the enforcement of unique constraints for columns requiring unique values.
"""
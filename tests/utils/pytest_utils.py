import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        if 'model_structure' in item.name:
            item.add_marker(pytest.mark.model_structure)
        if 'model' in item.name:
            item.add_marker(pytest.mark.model)
        if 'unit_schema' in item.name:
            item.add_marker(pytest.mark.unit_schema)
        if 'unit' in item.name:
            item.add_marker(pytest.mark.unit)
        if 'integrate' in item.name:
            item.add_marker(pytest.mark.integrate)
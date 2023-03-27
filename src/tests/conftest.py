import pytest


@pytest.fixture(scope='package')
def json_headers():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    yield headers

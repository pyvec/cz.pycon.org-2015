import pytest
from app import pycon_app


@pytest.fixture
def app():
    return pycon_app

import pytest

import config.sqlite

# Override the sqlite url to use an in memory database for testing
config.sqlite.DB_URL = "sqlite:///:memory:"

import flask.testing

from api import app as _raw_flask_app
from api import engine


@pytest.fixture()
def app():
    _raw_flask_app.testing = True
    assert str(engine.url) == "sqlite:///:memory:"
    # other setup can go here

    yield _raw_flask_app

    # clean up / reset resources here


@pytest.fixture()
def client(app) -> flask.testing.FlaskClient:
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

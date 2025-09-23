import os
import tempfile

import flask.testing
import pytest

# Override the database to use a temporary one
import config.sqlite

TEST_DIR = tempfile.TemporaryDirectory()
TEST_DB = os.path.join(TEST_DIR.name, "test.db")
config.sqlite.DB_URL = f"sqlite:///{TEST_DB}"
config.sqlite.DB_FILENAME = TEST_DB
from api import app as _raw_flask_app
from api.models import insert_user
from db_scripts.sqlite_setup import init_db


@pytest.fixture(scope="session")
def user_info():
    return {"username": "test_user", "password": "test_pass"}


@pytest.fixture(scope="session")
def app(user_info):
    _raw_flask_app.testing = True

    # Set up the database
    init_db()

    # Add a test user
    insert_user(user_info["username"], user_info["password"])

    # other setup can go here

    yield _raw_flask_app

    # clean up / reset resources here


@pytest.fixture()
def client(app) -> flask.testing.FlaskClient:
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

"""
Defines our setup for Pytest and fixtures shared by all of our tests

https://docs.pytest.org/en/stable/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files
"""

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

from dataclasses import dataclass

# The imports from api must go after the above block overriding the DB location
from api import app as _raw_flask_app
from api.models import insert_user
from db_scripts.sqlite_setup import init_db


@dataclass
class UserTestInfo:
    """
    Simple class to transmit user info in tests

    This is used because our main UserInfo does not store the
    plain text password for users to ensure security.
    """

    username: str
    password: str


@pytest.fixture(scope="session")
def user_info() -> UserTestInfo:
    """A Pytest fixture that provides data for the default test user"""
    return UserTestInfo(username="test_user", password="test_pass")


@pytest.fixture(scope="session")
def app(user_info: UserTestInfo):
    """
    A Pytest fixture that sets up our Flask app for testing.
    Use the client fixture below for tests.

    This fixture sets up the database and adds the user from user_info
    """
    _raw_flask_app.testing = True

    # Set up the database
    init_db()

    # Add a test user
    insert_user(user_info.username, user_info.password)

    # other setup can go here

    yield _raw_flask_app

    # clean up / reset resources here


@pytest.fixture()
def client(app) -> flask.testing.FlaskClient:
    """Main Pytest fixture to get access to a test client for our Flask app"""
    return app.test_client()

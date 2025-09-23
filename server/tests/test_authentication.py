from flask.testing import FlaskClient

from api.models import User


def test_index(client: FlaskClient):
    """Test basic index routing to see that we should get an HTML page"""
    result = client.get("/", follow_redirects=True)
    assert result.status_code == 200
    assert "<!DOCTYPE html>" in result.get_data().decode("utf-8")


def test_no_login(client: FlaskClient):
    """Test that we get an error from a secured endpoint without logging in"""
    result = client.get("/resource")
    assert result.status_code == 401


def test_login(client: FlaskClient, user_info):
    result = client.post(
        "/login",
        json={"username": user_info["username"], "password": user_info["password"]},
    )
    assert result.status_code == 200

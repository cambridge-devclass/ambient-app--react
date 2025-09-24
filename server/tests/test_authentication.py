from flask.testing import FlaskClient


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
    """
    Test that logging in allows us to access the protected resource

    client and user_info are both Pytest fixtures defined in the conftest.py file
    """
    login_result = client.post(
        "/login",
        json={"username": user_info["username"], "password": user_info["password"]},
    )
    assert login_result.status_code == 200

    result = client.get("/resource")
    assert result.status_code == 200
    json_data = result.json
    assert json_data is not None
    assert json_data == {"message": "Resource loaded"}


def test_logout_no_login(client: FlaskClient):
    """
    Test that logging out errors when a user is not logged in
    """
    bad_logout = client.post("/logout")
    assert bad_logout.status_code == 401


def test_logout_after_login(client: FlaskClient, user_info):
    """
    Test that logging out after a successful login revokes access to protected endpoints
    """
    # Ensure we're not logged in and can't access the protected resource. This just sanity
    # checks that the test starts in the state that we want it to.
    bad_access = client.get("/resource")
    assert bad_access.status_code == 401

    # Log in
    login_result = client.post(
        "/login",
        json={"username": user_info["username"], "password": user_info["password"]},
    )
    assert login_result.status_code == 200

    # Ensure we can access the resource
    good_access = client.get("/resource")
    assert good_access.status_code == 200

    # Ensure we can log out
    logout_result = client.post("/logout")
    assert logout_result.status_code == 200

    # After logout we should no longer be able to access the resource
    bad_access = client.get("/resource")
    assert bad_access.status_code == 401

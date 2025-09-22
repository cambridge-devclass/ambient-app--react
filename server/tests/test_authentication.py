from flask.testing import FlaskClient


def test_index(client: FlaskClient):
    """Test basic index routing to see that we should get an HTML page"""
    result = client.get("/", follow_redirects=True)
    assert result.status_code == 200
    assert "<!DOCTYPE html>" in result.get_data().decode("utf-8")

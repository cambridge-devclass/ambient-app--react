from flask.testing import FlaskClient


def test_api_spec(client: FlaskClient):
    """
    Ensure that the Swagger API doc loads

    Just checking the status code is sufficient as a sanity check to ensure there are no errors.
    If this test fails, there is likely a syntax error in the yaml comments for one of the routes.
    Pasting the doc comment into an online YAML checker can help debug issues.
    """
    result = client.get("/spec")
    assert result.status_code == 200

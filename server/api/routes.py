"""
Definition of routes for our Flask API

Routes are various URLs in the API that the frontend can make HTTP requests to.

These routes (aka endpoints) provide various backend services like user logins and database access.
"""

import flask
from flask import jsonify, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_swagger import swagger

from api import app
from api.models import get_user_by_name, insert_user


@app.route("/")
def index():
    """
    Return app's index page
    ---
    responses:
      200:
        description: Index page
    """
    return redirect(url_for("static", filename="index.html"))


@app.route("/login", methods=["POST"])
def login():
    """
    Login endpoint. Establishes a session after successful login.
    ---
    parameters:
      - in: body
        name: body
        schema:
          id: User
          required:
            - username
            - password
          properties:
            username:
              type: string
              description: User name
            password:
              type: string
              description: Password for user

    responses:
      200:
        description: Successful login. Session established
      400:
        description: Invalid data or request
      401:
        description: Unsuccessful login.
    """

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username is None or password is None:
        return "username or password not specified", 400

    user = get_user_by_name(username)
    if user is None or not user.check_password(password):
        return "Invalid username or password", 401

    # flask_login and this call to login_user handles the session for us
    if not login_user(user):
        return (
            "There was a problem logging in, your account may have been deactivated.",
            401,
        )

    return "", 200


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    """
    Logout endpoint. You must be logged in via /login to use this.

    TODO fill out details
    ---
    responses:
      200:
        description: Successful logout. Session deleted.
      401:
        description: Unsuccessful logout. User was not logged in.
    """
    logout_user()
    return "", 200


@app.route("/user", methods=["POST"])
def add_user():
    """
    Add user endpoint.

    Username must be unique and nonempty, password must be nonempty
    ---
    parameters:
      - in: body
        name: user_data
        required:
          - username
            password
            confirm_password
        description: user/pass info
        properties:
          username:
            type: string
            description: Name to look up for user
          password:
            type: string
            description: Plaintext password
          confirm_password:
            type: string
            decription: Should match password
    responses:
      201:
        description: Successfully created user record
      400:
        description: Invalid data or request

    """
    try:
        params = request.get_json()
        if params["password"] != params["confirm_password"]:
            raise Exception("Password fields must match")

        insert_user(params["username"], params["password"])
        return "", 201
    except Exception as e:
        # todo(?), return more helpful error messages to client
        return str(e), 400


@app.route("/resource")
@login_required
def get_resource():
    """
    Sample endpoint depending on having logged in with /login

    Ensure that you've successfully logged in using /login. The session cookie should be in the user's browser.
    ---
    responses:
      200:
        description: Valid session. Returns test HTML.
      401:
        description: Invalid or non-existent user session.
    """
    return jsonify({"message": "Resource loaded"}), 200


@app.route("/sample/<int:id>", methods=["POST"])
def get_sample(id: int):
    """
    Sample endpoint taking a path parameter, body data, and query parameter.

    Form and header data are also available

    The doc string below is YAML for OpenAPI v2.0

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md

    E.g. here is the spec on documenting API parameters

    https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#parameter-object
    ---
    parameters:
      - in: path
        name: id
        description: An id for the sample resource we'll look up
        required: true
      - in: body
        name: data
        description: Some bigger data passed to the request body
        required: true
        required:
              - data
        properties:
          data:
            type: string
            description: Test string data
      - in: query
        name: option
        description: Some small flag passed as a query string
        required: true
    responses:
      200:
        description: Valid session. Returns test JSON.
    """
    return {
        "message": f"Data for passed id={id}, body data={request.get_json().get("data")}, query={request.args.get("option")}"
    }


@app.route("/spec")
def spec():
    """
    Return the Swagger specification.
    ---
    responses:
      200:
        description: A Swagger specification.
    """
    swag = swagger(app)
    swag["info"]["title"] = "Ambient App Backend"
    swag["info"]["version"] = "v0.0.1"
    return jsonify(swag)

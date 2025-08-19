"""
Definition of routes for our Flask API

Routes are various URLs in the API that the frontend can make HTTP requests to.

These routes (aka endpoints) provide various backend services like user logins and database access.
"""

from api import app
from flask import session, jsonify, render_template, url_for, redirect
import flask
from flask_swagger import swagger


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

    TODO fill out details
    ---
    responses:
      200:
        description: Successful login. Session established
      401:
        description: Unsuccessful login.
    """
    session["token"] = "test token"
    return "<p>WIP!</p>"


@app.route("/logout", methods=["POST"])
def logout():
    """
    Logout endpoint. You must be logged in via /login to use this.

    TODO fill out details
    ---
    responses:
      200:
        description: Successful login. Session deleted.
      401:
        description: Unsuccessful logout. User was not logged in.
    """
    session.pop("token", default=None)
    return ""


@app.route("/resource")
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
    # Example endpoint using a session. Post to /login first, store the cookie,
    # and send the cookie with a get to /resource to test. E.g.
    #
    #   curl -X POST http://127.0.0.1:5000/login -c cookies.txt
    #   curl -b cookies.txt -X GET http://127.0.0.1:5000/resource
    if session.get("token") != "test token":
        # Return 401 Unauthorized
        return "", 401
    return "<p>Your data</p>"


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

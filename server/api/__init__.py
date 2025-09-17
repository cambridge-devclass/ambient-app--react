"""
Set up the root Flask app

See other modules in this package (i.e. folder) for functionality
"""

import os
import secrets

from flask import Flask
from flask_login import LoginManager
from flask_swagger_ui import get_swaggerui_blueprint


def get_or_create_secret_key():
    "Read in the Flask secret key from the filesystem or generate a new one if the file is not found"
    folder_name = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(folder_name, "flask_secret_key.txt")
    # Try to read the key
    try:
        with open(file_name, "r") as f:
            key = f.read().strip()
    except:
        # Generate a new key and save it in the file
        key = secrets.token_hex()
        with open(file_name, "w") as f:
            f.write(key)

    return key


# Start the Flask app
app = Flask(__name__)

# Set secret key to enable session usage
app.secret_key = get_or_create_secret_key()

# Configure Swagger UI blueprint to show interactive API doc
SWAGGER_URL = "/swagger-ui"
API_URL = "/spec"  # Endpoint for your Swagger JSON
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Ambient App Backend"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# Use sqlalchemy to connect to db
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Get the db url from config file
from config.sqlite import DB_URL

# Set autocommit to false, requiring
# explicit calls to session.commit()
engine = create_engine(
    DB_URL, connect_args={"autocommit": False}
)

# Session provides api for executing queries
session = Session(engine)


# Configure login management
login = LoginManager(app)

from api import routes

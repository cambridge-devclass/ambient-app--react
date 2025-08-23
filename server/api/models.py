"""
Models used in the backend
"""

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from api import login


class User(UserMixin):
    def __init__(self, id, name, password) -> None:
        self.id: int = id
        self.username: str = name
        self.password_hash: str = ""
        self.set_password(password)

    def set_password(self, password: str):
        "Set the user's password updating the stored hash"
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        "Check to see if the provided password matches the provided password"
        return check_password_hash(self.password_hash, password)


ALL_USERS = [
    User(1, "test1", "test password"),
    User(2, "test2", "other password"),
]


def get_user_by_name(name: str) -> User | None:
    for user in ALL_USERS:
        if user.username == name:
            return user
    return None


@login.user_loader
def load_user(id: str) -> User | None:
    "Function used by Flask-Login to find a user. TODO hook to database"
    for user in ALL_USERS:
        if str(user.id) == id:
            return user
    return None

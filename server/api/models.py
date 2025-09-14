"""
Models used in the backend
"""

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from api import login, session

from sqlalchemy import select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    def save(self) -> None:
        "Commit any changes to this model to the db"
        session.add(self)
        session.commit()

class User(Base, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column()

    def __init__(self, name) -> None:
        self.username = name

    def set_password(self, password: str) -> None:
        "Set the user's password updating the stored hash"
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        "Check to see if the provided password matches the correct user password"
        return check_password_hash(self.password_hash, password)


def get_user_by_name(name: str) -> User | None:
    stmt = select(User).filter_by(username=name)
    return session.scalars(stmt).first()
    

@login.user_loader
def load_user(id: str) -> User | None:
    "Function used by Flask-Login to find a user"
    stmt = select(User).filter_by(id=id, is_active=1)
    return session.scalars(stmt).first()


def insert_user(username: str, password: str) -> User:
    "Create a new user model and add to the db"
    existing = get_user_by_name(username)
    if existing is not None:
        raise Exception("There is already a user with that username")

    new_user = User(username)
    new_user.set_password(password)
    new_user.save()

    return new_user

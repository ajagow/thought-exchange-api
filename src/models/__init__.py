from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db


db = SQLAlchemy()
bcrypt = Bcrypt()

from .PostModel import PostModel, PostSchema
from .UserModel import UserModel, UserSchema
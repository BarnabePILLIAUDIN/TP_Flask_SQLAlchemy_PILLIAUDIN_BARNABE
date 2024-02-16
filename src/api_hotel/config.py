import os

config = {
    "database_uri": os.environ['DATABASE_URI'],
    "'SQLALCHEMY_TRACK_MODIFICATIONS'": False
}

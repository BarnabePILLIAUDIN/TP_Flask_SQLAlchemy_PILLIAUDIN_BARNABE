import os

config = {
    "database_uri": os.environ['DATABASE_URI'],
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    "max_number_of_seeds": 10
}

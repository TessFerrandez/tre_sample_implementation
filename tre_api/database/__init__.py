from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def reset_database():
    from tre_api.database.models import Schema
    db.drop_all()
    db.create_all()

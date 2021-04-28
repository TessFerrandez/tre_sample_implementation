from tre_api.database import db
from tre_api.database.models import Schema


def create_schema(data: dict):
    schema_id = data.get('id')
    schema = Schema(schema_id)
    schema.format = data.get('format')
    schema.version = data.get('version')
    schema.schema = data.get('schema')
    schema.resource_type = data.get('resource_type')
    db.session.add(schema)
    db.session.commit()


def update_schema(schema_id: str, data: dict):
    schema = Schema.query.filter(Schema.id == schema_id).one()
    schema.format = data.get('format')
    schema.schema = data.get('schema')
    schema.version = data.get('version')
    schema.resource_type = data.get('resource_type')
    db.session.add(schema)
    db.session.commit()


def delete_schema(schema_id):
    schema = Schema.query.filter(Schema.id == schema_id).one()
    db.session.delete(schema)
    db.session.commit()

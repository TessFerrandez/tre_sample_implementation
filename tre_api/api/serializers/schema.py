from flask_restplus import fields
from tre_api.api.restplus import api


schema = api.model('Schema', {
    'id': fields.String(readOnly=True, description='The unique identifier of a schema'),
    'format': fields.String(required=True, description='schema format (ex. jsonschema)'),
    'version': fields.String(required=True, description='schema version (ex. v1)'),
    'resource_type': fields.String(required=True, description='resource type (ex. Workspace'),
    'schema': fields.String(required=True, description='the schema itself'),
})

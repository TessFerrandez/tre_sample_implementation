import logging

from flask import request
from flask_restplus import Resource
from tre_api.api.restplus import api
from tre_api.api.serializers.schema import schema
from tre_api.database.models import Schema
from tre_api.api.business.schema import create_schema, update_schema, delete_schema


log = logging.getLogger(__name__)
ns = api.namespace('schemas', description='Operations related to schemas')


@ns.route('/')
class SchemaCollection(Resource):
    @api.marshal_list_with(schema)
    def get(self):
        """
        Returns a list of schemas
        """
        schemas = Schema.query.all()
        return schemas

    @api.response(201, 'Schema successfully created.')
    @api.expect(schema)
    def post(self):
        """
        Creates a new schema
        """
        data = request.json
        create_schema(data)
        return None, 201


@ns.route('/<id>')
@api.response(404, 'Schema not found')
class SchemaItem(Resource):
    @api.marshal_with(schema)
    def get(self, id: str):
        """
        Returns a schema
        """
        return Schema.query.filter(Schema.id == id).one()

    @api.expect(schema)
    @api.response(204, 'Schema successfully updated.')
    def put(self, id: str):
        """
        Updates a schema

        Use this method to change the version of a schema.

        * Send a JSON object with the new version in the request body.

        ```
        {
          "version": "v2"
        }
        ```

        * Specify the ID of the version to modify in the request URL path.
        """
        data = request.json
        update_schema(id, data)
        return None, 204

    @api.response(204, 'Schema successfully deleted.')
    def delete(self, id: str):
        """
        Deletes a schema
        """
        delete_schema(id)
        return None, 204

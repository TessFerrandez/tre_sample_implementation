"""
Configures the base swagger for the API - and sets up error handlers
"""
import logging
import traceback

from flask_restplus import Api
from tre_api import settings
from sqlalchemy.orm.exc import NoResultFound


log = logging.getLogger(__name__)
api = Api(version='0.1', title='Azure TRE API', description='A sample implementation of the Azure TRE API')


@api.errorhandler
def default_error_handler(e):
    """Global error handler"""
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    """No results found in database"""
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404

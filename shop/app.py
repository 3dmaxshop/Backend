import logging

from flask import Flask
from pydantic import ValidationError

from shop.db import db_session
from shop.errors import AppError
from shop.views import categories, models, users

logger = logging.getLogger(__name__)


def handle_app_errors(error: AppError):
    err = {'error': error.reason}, error.status
    logger.warning('error occurred: $s', str(err))
    return err


def handle_validation_errors(error: ValidationError):
    logger.warning(str(error))
    return {'error': error.errors()}, 422


def shutdown_session(exception=None):
    db_session.remove()


app = Flask(__name__)
app.register_error_handler(AppError, handle_app_errors)
app.register_error_handler(ValidationError, handle_validation_errors)
app.register_blueprint(models.routes, url_prefix='/api/v1/models')
app.register_blueprint(categories.routes, url_prefix='/api/v1/categories')
app.register_blueprint(users.routes, url_prefix='/api/v1/users')
app.teardown_appcontext(shutdown_session)

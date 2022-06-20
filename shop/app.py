import logging

from flask import Flask

from shop.errors import AppError
from shop.views import models

logger = logging.getLogger(__name__)


def handle_app_errors(error: AppError):
    err = {'error': error.reason}, error.status
    logger.warning('error occurred: $s', str(err))
    return err


app = Flask(__name__)
app.register_error_handler(AppError, handle_app_errors)
app.register_blueprint(models.routes, url_prefix='/api/v1/models')

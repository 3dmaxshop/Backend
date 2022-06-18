from flask import Flask

from shop.errors import AppError
from shop.views import models


def handle_app_errors(error: AppError):
    return {'error': error.reason}, error.status


app = Flask(__name__)

app.register_error_handler(AppError, handle_app_errors)
app.register_blueprint(models.routes, url_prefix='/api/v1/models')

if __name__ == '__main__':
    app.run()

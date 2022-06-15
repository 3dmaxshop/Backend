from flask import Flask, abort
from shop.errors import AppError
from shop.views import models



def handle_app_errors(error: AppError):
    # Это работает
    # |
    # v
    return {'error': error.reason}, error.status
    # Это не работает
    # |
    # v
    #abort(int(error.status), str(error.reason))
    

app = Flask(__name__)

app.register_error_handler(AppError, handle_app_errors)
app.register_blueprint(models.routes, url_prefix='/api/v1/models')

if __name__ == '__main__':
    app.run()
from flask import Flask
from shop.views import models

app = Flask(__name__)

app.register_blueprint(models.routes, url_prefix='/api/v1/models')

if __name__ == '__main__':
    app.run()
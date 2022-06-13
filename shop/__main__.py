from flask import Flask
from shop import server

app = Flask(__name__)

app.register_blueprint(server.routes, url_prefix='/api/v1/models')

if __name__ == '__main__':
    app.run()
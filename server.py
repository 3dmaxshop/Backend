from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '3dMaxShop'

if __name__ == "__main__":
    app.run()
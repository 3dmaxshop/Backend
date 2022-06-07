from flask import Flask
import json

app = Flask(__name__)

models = [{'name': 'sofa1','color': 'blue','catigories': 'sofa',},
           {'name': 'sofa2','color': 'red','catigories': 'sofa',}]

@app.get('/api/v1/models/')
def get_models():
    return json.dumps(models)

if __name__ == '__main__':
    app.run(debug=True)
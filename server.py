from flask import Flask, request
import json

app = Flask(__name__)

models = [{'name': 'sofa1','color': 'blue','catigories': 'sofa',},
           {'name': 'sofa2','color': 'red','catigories': 'sofa',}]

def hcesk_model_name_in_models(payload, models):
    for model in models:
        if payload['name'] == model['name']:
            return False
    return True


@app.get('/api/v1/models/')
def get_models():
    return json.dumps(models)

@app.post('/api/v1/models/')
def add_model():
    payload = request.json
    if hcesk_model_name_in_models(payload, models):
        models.append(payload)
        return payload
    return "Модель с таким именем уже есть в базе"
    

if __name__ == '__main__':
    app.run(debug=True)
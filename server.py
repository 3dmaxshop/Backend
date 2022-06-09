from pyexpat import model
from flask import Flask, request
import json

app = Flask(__name__)

models = [{'id': 0, 'name': 'sofa1','color': 'blue','catigories': 'sofa',},
           {'id': 1,'name': 'sofa2','color': 'red','catigories': 'sofa',}]

def check_model_name_in_unique(payload, models):
    for model in models:
        if payload['name'] == model['name']:
            return False
    return True

def check_model_id_in_unique(model_id, models):
    for model in models:
        if model['id'] == model_id:
            return model
    return False

zero_model_id = 0

#GET /api/v1/models/1 - получить модель с ид. 1

@app.get('/api/v1/models/<int:model_id>')
def get_model_from_id(model_id):
    id_model = model_id
    model = check_model_id_in_unique(model_id, models)
    if model == False:
        return json.dumps([{'Error': f'Модель с id: {model_id} не найдена в базе'}])
    return json.dumps(model)

@app.get('/api/v1/models/')
def get_models():
    return json.dumps(models)

@app.post('/api/v1/models/')
def add_model():
    payload = request.json
    if not check_model_name_in_unique(payload, models):
        return json.dumps([{"Error": "Модель с таким именем уже есть в базе"}])
    payload['id'] = models[-1]['id'] + 1
    models.append(payload)
    return payload
    
    

if __name__ == '__main__':
    app.run(debug=True)
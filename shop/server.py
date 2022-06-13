from flask import Flask, request, abort
import json
from storage import Storage

app = Flask(__name__)

storage = Storage()

@app.delete('/api/v1/models/<int:model_id>')
def delete_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    if not model:
        return json.dumps([{'Error': f'Модель с id: {model_id} не найдена в базе'}])
    storage.delete(model_id)
    return json.dumps([{'result': f'Модель с id: {model_id} удалена'}])

@app.get('/api/v1/models/<int:model_id>')
def get_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    if not model:
        return json.dumps([{'Error': f'Модель с id: {model_id} не найдена в базе'}])
    return json.dumps(model)

@app.get('/api/v1/models/')
def get_models():
    return json.dumps(storage.get_all())

@app.post('/api/v1/models/')
def add_model():
    payload = request.json
    if not storage.check_model_name_unique(payload["name"]):
        abort(409,"Модель с таким именем уже есть в базе")
    storage.add(payload)
    return payload

@app.put('/api/v1/models/<int:model_id>')
def change_model(model_id):
    payload = request.json
    change_model = storage.change(model_id, payload)
    if change_model == "Model_dublicate_eror":
        return abort(409,"Модель с таким именем уже есть в базе")
    return change_model


    
    


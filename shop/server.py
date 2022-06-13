from unicodedata import name
from flask import Flask, request, abort
import json

app = Flask(__name__)

class Storage:
    def __init__(self):
        self.models = {}
        self.model_names = set()
        self.last_id = 0

    def check_model_name_unique(self,name):
        return name not in self.model_names
         
    def get_by_id(self, model_id):
        return self.models.get(model_id)

    def delete(self, model_id):
        model = self.models[model_id]
        model_name = model['name']
        self.model_names.remove(model_name)
        self.models.pop(model_id)
    
    def get_all(self):
        return list(self.models.values())

    def add(self, model):
        self.last_id += 1
        model['id'] = self.last_id
        self.models[model['id']] = model
        self.model_names.add(model['name'])

    def change(self, model_id, change_model) -> dict:
        # Проверить изменилось ли имя модели
        old_name = self.models[model_id]['name']
        new_name = change_model['name']

        if old_name == new_name:
            self.models[model_id] = change_model
            self.models[model_id]['id'] = model_id
            return self.models[model_id]

        if old_name != new_name and self.check_model_name_unique(new_name):
            self.model_names.remove(old_name)
            self.model_names.add(new_name)
            self.models[model_id] = change_model
            self.models[model_id]['id'] = model_id
            return self.models[model_id]
            
        return abort(409,"Модель с таким именем уже есть в базе")


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
    return change_model


    
    


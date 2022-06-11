from unicodedata import name
from flask import Flask, request, abort
import json
from shop.models import models_list

app = Flask(__name__)





class Storage:
    def __init__(self, models):
        self.models = {model['id']: model for model in models}
        self.model_names = {model['name'] for model in models}
        self.last_id = 0

    def check_model_name_unique(self,name):
        return name not in self.model_names
         
    def get_by_id(self, model_id):
        return self.models.get(model_id)

    def delete(self, model_id):
        model = self.models[model_id]
        self.model_names.pop(model['name'])
        self.models.pop(model_id)
    
    def get_all(self):
        return list(self.models.values())

    def add(self, model):
        self.last_id += 1
        model['id'] = self.last_id
        self.models[model['id']] = model
        self.model_names = model['name']

storage = Storage(models_list)

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
    if not storage.check_model_name_unique(payload):
        abort(409,"Модель с таким именем уже есть в базе")
    storage.add(payload)
    return payload
    
    

if __name__ == '__main__':
    app.run(debug=True)
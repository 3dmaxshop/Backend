from flask import request, Blueprint
import json
from shop.storage import Storage

storage = Storage()

routes = Blueprint('models', __name__)

@routes.delete('/<int:model_id>')
def delete_model_from_id(model_id):
    storage.delete(model_id)
    return {}, 204
    

@routes.get('/<int:model_id>')
def get_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    return json.dumps(model)

@routes.get('/')
def get_models():
    return json.dumps(storage.get_all())

@routes.post('/')
def add_model():
    payload = request.json
    model = storage.add(payload)
    return model

@routes.put('/<int:model_id>')
def change_model(model_id):
    payload = request.json
    return storage.change(model_id, payload)
   



    
    


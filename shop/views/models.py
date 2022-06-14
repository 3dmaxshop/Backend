from ast import Return
from flask import Flask, request, abort, Blueprint
import json
from shop.storage import Storage

storage = Storage()

routes = Blueprint('models', __name__)

@routes.delete('/<int:model_id>')
def delete_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    if not model:
        abort (404, "model not found")
    storage.delete(model_id)
    return {}, 204
    

@routes.get('/<int:model_id>')
def get_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    if not model:
        abort (404, "model not found")
    return json.dumps(model)

@routes.get('/')
def get_models():
    return json.dumps(storage.get_all())

@routes.post('/')
def add_model():
    payload = request.json
    if not storage.check_model_name_unique(payload["name"]):
        abort(409,"Модель с таким именем уже есть в базе")
    storage.add(payload)
    return payload

@routes.put('/<int:model_id>')
def change_model(model_id):
    payload = request.json
    try:
        return storage.change(model_id, payload)
    except ValueError as err:
        abort(400, str(err))



    
    


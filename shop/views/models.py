from ast import Return
from xml.dom import NotFoundErr
from flask import Flask, request, abort, Blueprint
import json
from shop.errors import AppError,NotFoundError, Conflict
from shop.storage import Storage

storage = Storage()

routes = Blueprint('models', __name__)

@routes.delete('/<int:model_id>')
def delete_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    if not model:
        raise NotFoundError('',f'model {model_id} not found')
    storage.delete(model_id)
    return {}, 204
    

@routes.get('/<int:model_id>')
def get_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    if not model:
        raise NotFoundError('',f'model {model_id} not found')
    return json.dumps(model)

@routes.get('/')
def get_models():
    return json.dumps(storage.get_all())

@routes.post('/')
def add_model():
    payload = request.json
    model_name = payload["name"]
    if not storage.check_model_name_unique(model_name):
        raise Conflict(model_name, f'reason: model name {model_name} is not unique')
    storage.add(payload)
    return payload

@routes.put('/<int:model_id>')
def change_model(model_id):
    payload = request.json
    return storage.change(model_id, payload)
   



    
    


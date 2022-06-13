from flask import Flask, request, abort, Blueprint
import json
from storage import Storage

storage = Storage()

routes = Blueprint('server', __name__)

@routes.delete('/<int:model_id>')
def delete_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    if not model:
        return json.dumps([{'Error': f'Модель с id: {model_id} не найдена в базе'}])
    storage.delete(model_id)
    return json.dumps([{'result': f'Модель с id: {model_id} удалена'}])

@routes.get('/<int:model_id>')
def get_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    if not model:
        return json.dumps([{'Error': f'Модель с id: {model_id} не найдена в базе'}])
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
    change_model = storage.change(model_id, payload)
    if change_model == "Model_dublicate_eror":
        return abort(409,"Модель с таким именем уже есть в базе")

    if change_model == "Index_not_found_eror":
        return abort(409,"Модель c указанным индексом не существует")
   
    return change_model


    
    


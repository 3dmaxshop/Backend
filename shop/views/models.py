import json
import logging

from flask import Blueprint, request

from shop.schemas import Model
from shop.sqlstorage import Storage

logger = logging.getLogger(__name__)

storage = Storage()

routes = Blueprint('models', __name__)


@routes.post('/')
def add_model():
    payload = request.json
    payload['uid'] = -1
    logger.debug('add model')
    model = storage.add(Model(**payload))
    return json.dumps(model)


@routes.get('/<int:model_id>')
def get_model_from_uid(model_id):
    model = storage.get_by_uid(model_id)
    logger.debug('get model from uid')
    return json.dumps(Model.from_orm(model).dict())


@routes.get('/')
def get_all_models():
    return json.dumps(storage.get_all())


@routes.delete('/<int:model_id>')
def delete_model(model_id):
    storage.delete_model_from_uid(model_id)
    logger.debug('delete model')
    return {}, 204


@routes.put('/')
def change_model():
    payload = request.json
    model = Model(**payload)
    change_model = storage.change(model)
    logger.debug('change model')
    return json.dumps(change_model)

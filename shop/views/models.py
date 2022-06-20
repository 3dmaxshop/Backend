import json
import logging

from flask import Blueprint, request

from shop.storage import Storage

logger = logging.getLogger(__name__)

storage = Storage()

routes = Blueprint('models', __name__)


@routes.delete('/<int:model_id>')
def delete_model_from_id(model_id):
    storage.delete(model_id)
    logger.debug('delete model')
    return {}, 204


@routes.get('/<int:model_id>')
def get_model_from_id(model_id):
    model = storage.get_by_id(model_id)
    logger.debug('get model from id')
    return json.dumps(model)


@routes.get('/')
def get_models():
    logger.debug('get all models')
    return json.dumps(storage.get_all())


@routes.post('/')
def add_model():
    payload = request.json
    logger.debug('add model')
    return storage.add(payload)


@routes.put('/<int:model_id>')
def change_model(model_id):
    payload = request.json
    logger.debug('change model')
    return storage.change(model_id, payload)

import logging

import orjson
from flask import Blueprint, request

from shop.schemas import Model
from shop.storage import Storage

logger = logging.getLogger(__name__)

storage = Storage()

routes = Blueprint('models', __name__)


@routes.delete('/<int:model_id>')
def delete_model_from_uid(model_id):
    storage.delete(model_id)
    logger.debug('delete model')
    return {}, 204


@routes.get('/<int:model_id>')
def get_model_from_uid(model_id):
    model = storage.get_by_uid(model_id)
    logger.debug('get model from uid')
    return orjson.dumps(model)


@routes.get('/')
def get_models():
    logger.debug('get all models')
    return orjson.dumps(storage.get_all())


@routes.post('/')
def add_model():
    payload = request.json
    payload['uid'] = -1
    model = Model(**payload)
    logger.debug('add model')
    return storage.add(model.dict())


@routes.put('/<int:model_id>')
def change_model(model_id):
    payload = request.json
    model = Model(**payload)
    logger.debug('change model')
    return storage.change(model_id, model.dict())

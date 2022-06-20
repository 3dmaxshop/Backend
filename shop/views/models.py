import orjson
import logging

from flask import Blueprint, request

from shop.schemas import CorrectModel
from shop.storage import Storage

logger = logging.getLogger(__name__)

storage = Storage()

routes = Blueprint('models', __name__)


@routes.delete('/<int:model_uid>')
def delete_model_from_uid(model_uid):
    storage.delete(model_uid)
    logger.debug('delete model')
    return {}, 204


@routes.get('/<int:model_uid>')
def get_model_from_uid(model_uid):
    model = storage.get_by_uid(model_uid)
    logger.debug('get model from uid')
    return model.json()


@routes.get('/')
def get_models():
    logger.debug('get all models')
    return orjson.dumps(storage.get_all())


@routes.post('/')
def add_model():
    payload = request.json
    payload['uid'] = -1
    model = CorrectModel(**payload)
    logger.debug('add model')
    return storage.add(model.dict())


@routes.put('/<int:model_uid>')
def change_model(model_uid):
    payload = request.json
    model = CorrectModel(**payload)
    logger.debug('change model')
    return storage.change(model_uid, model.dict())

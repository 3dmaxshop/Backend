import logging

import orjson
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
    model = Model(**payload)
    logger.debug('add model')
    return storage.add(model.dict())

import json
import logging

from flask import Blueprint, request

from shop.schemas import Category
from shop.sqlstorage import Storage

logger = logging.getLogger(__name__)

storage = Storage()

routes = Blueprint('categories', __name__)


@routes.get('/')
def get_all_categories():
    return json.dumps(storage.get_all_categories())


@routes.post('/')
def add_category():
    payload = request.json
    payload['uid'] = -1
    logger.debug('add categories')
    category = storage.add_category(Category(**payload))
    return json.dumps(category)

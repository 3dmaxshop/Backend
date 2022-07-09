import json
import logging

from flask import Blueprint, request

from shop.categoryStorage import CategoryStorage
from shop.schemas import Category

logger = logging.getLogger(__name__)

categoryStorage = CategoryStorage()

routes = Blueprint('categories', __name__)


@routes.get('/')
def get_all_categories():
    return json.dumps(categoryStorage.get_all_categories())


@routes.post('/')
def add_category():
    payload = request.json
    payload['uid'] = -1
    logger.debug('add categories')
    category = categoryStorage.add_category(Category(**payload))
    return json.dumps(category)

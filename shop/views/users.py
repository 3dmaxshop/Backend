import json
import logging

from flask import Blueprint, request

from shop.schemas import User
from shop.usersstorage import UsersStorage

logger = logging.getLogger(__name__)

usersStorage = UsersStorage()

routes = Blueprint('users', __name__)


@routes.get('/')
def get_all_categories():
    return json.dumps(usersStorage.get_all_categories())


@routes.post('/')
def add_category():
    payload = request.json
    payload['id'] = -1
    logger.debug('add users')
    user = usersStorage.add_user(User(**payload))
    return json.dumps(user)

import json
import logging

from flask import Blueprint, request

from shop.schemas import User
from shop.usersstorage import UsersStorage

logger = logging.getLogger(__name__)

usersStorage = UsersStorage()

routes = Blueprint('users', __name__)


@routes.post('/')
def add_user():
    payload = request.json
    payload['id'] = -1
    logger.debug('add users')
    user = usersStorage.add_user(User(**payload))
    return json.dumps(user)


@routes.post('/checkauthorization/')
def check_user():
    payload = request.json
    user = User(**payload)
    logger.debug('check users')
    user_authorization = usersStorage.check_user_password(user)
    if user_authorization:
        return json.dumps('True')
    return json.dumps('False')

from sqlalchemy.exc import IntegrityError

from shop.db import db_session
from shop.dbmodels import Users
from shop.errors import ConflictError, NotFoundError
from shop.schemas import User


class UsersStorage:

    def add_user(self, user: User):
        new_model = Users(
            username=user.username,
            password=user.password,
            role=user.role,
        )

        new_model.set_password(user.password)

        try:
            db_session.add(new_model)
            db_session.commit()
        except IntegrityError:
            raise ConflictError('user', f'name: {user.username}')
        return User.from_orm(new_model).dict()

    def check_user_password(self, user: User):
        user_in_db = Users.query.filter(Users.username == user.username).first()
        if not user_in_db:
            raise NotFoundError('user', f'uid: {user.username}')
        if user_in_db.check_password(user.password):
            return User.from_orm(user_in_db).dict()
        return False

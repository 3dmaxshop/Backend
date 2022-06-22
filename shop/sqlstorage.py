from typing import Any

from shop.db import db_session
from shop.dbmodels import Models
from shop.errors import ConflictError, NotFoundError
from shop.schemas import Model


class Storage:

    def add(self, model: Model):
        new_model = Models(
            name=model.name,
            color=model.color,
            catigories=model.catigories,
        )
#        company = Company.query.filter(Company.uid == uid).first()

        if Models.query.filter(Models.name == model.name).first():
            raise ConflictError('model', f'name: {model.name}')
        db_session.add(new_model)
        db_session.commit()

        return Model.from_orm(new_model).dict()

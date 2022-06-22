from typing import Any

from shop.db import db_session
from shop.dbmodels import Models
from shop.errors import ConflictError, NotFoundError
from shop.schemas import Model


class Storage:

    def add(self, model: Models):
        new_model = Models(
            name=model.name,
            color=model.color,
            catigories=model.catigories,
        )
        db_session.add(new_model)
        db_session.commit()

        return Model.from_orm(new_model).dict()

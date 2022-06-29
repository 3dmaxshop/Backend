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
        if Models.query.filter(Models.name == model.name).first():
            raise ConflictError('model', f'name: {model.name}')
        db_session.add(new_model)
        db_session.commit()
        return Model.from_orm(new_model).dict()

    def get_by_uid(self, model_id):
        model = Models.query.filter(Models.uid == model_id).first()
        if not model:
            raise NotFoundError('model', f'uid: {model_id}')
        return model

    def get_all(self):
        return [Model.from_orm(model).dict() for model in Models.query.all()]

    def delete_model_from_uid(self, model_id):
        model = Models.query.filter(Models.uid == model_id).first()
        if not model:
            raise NotFoundError('model', f'uid: {model_id}')

        db_session.delete(model)
        db_session.commit()

    def change(self, change_model):
        model = Models.query.filter(Models.uid == change_model.uid).first()
        if not model:
            raise NotFoundError('model', f'uid: {change_model.uid}')

        if Models.query.filter(Models.name == change_model.name, Models.uid != change_model.uid).first():
            raise ConflictError('model', f'name: {model.name}')
        model.name = change_model.name
        model.color = change_model.color
        model.catigories = change_model.catigories

        db_session.commit()

        return Model.from_orm(model).dict()

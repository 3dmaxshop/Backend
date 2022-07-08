from sqlalchemy.exc import IntegrityError

from shop.db import db_session
from shop.dbmodels import Categories, Models
from shop.errors import ConflictError, NotFoundError
from shop.schemas import Category, Model


class Storage:

    def add(self, model: Model):
        new_model = Models(
            name=model.name,
            color=model.color,
            categories=model.categories,
        )
        try:
            db_session.add(new_model)
            db_session.commit()
        except IntegrityError:
            raise ConflictError('model', f'name: {model.name}')
        return Model.from_orm(new_model).dict()

    def add_category(self, categories: Category):
        new_categories = Categories(
            name=categories.name,
        )
        try:
            db_session.add(new_categories)
            db_session.commit()
        except IntegrityError:
            raise ConflictError('categories', f'name: {categories.name}')
        return Category.from_orm(new_categories).dict()

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

        model.name = change_model.name
        model.color = change_model.color
        model.categories = change_model.categories

        try:
            db_session.commit()
        except IntegrityError:
            raise ConflictError('model', f'name: {change_model.name}')
        return Model.from_orm(model).dict()

    def get_all_categories(self):
        return [Categories.from_orm(categories).dict() for categories in Categories.query.all()]

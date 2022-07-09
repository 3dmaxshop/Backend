from sqlalchemy.exc import IntegrityError

from shop.db import db_session
from shop.dbmodels import Categories
from shop.errors import ConflictError, NotFoundError
from shop.schemas import Category


class CategoryStorage:

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

    def get_all_categories(self):
        return [Category.from_orm(categories).dict() for categories in Categories.query.all()]

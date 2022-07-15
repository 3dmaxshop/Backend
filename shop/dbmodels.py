from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

from shop.db import Base, engine


class Categories(Base):
    __tablename__ = 'categories'

    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    models = relationship('Models')


class Models(Base, UserMixin):
    __tablename__ = 'models'

    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    color = Column(String, nullable=False)
    category_id = Column(Integer(), ForeignKey(Categories.uid), nullable=True)

    def __repr__(self) -> str:
        return f'Models {self.uid} {self.name} {self.color} {self.categories_id}'


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

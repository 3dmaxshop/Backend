from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from shop.db import Base, engine


class Categories(Base):
    __tablename__ = 'categories'

    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    models = relationship('Models')


class Models(Base):
    __tablename__ = 'models'

    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    color = Column(String, nullable=False)
    category_id = Column(Integer(), ForeignKey(Categories.uid), nullable=True)

    def __repr__(self) -> str:
        return f'Models {self.uid} {self.name} {self.color} {self.categories_id}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

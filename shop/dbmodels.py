from sqlalchemy import Column, Integer, String

from shop.db import Base, engine


class Models(Base):
    __tablename__ = 'models'

    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    color = Column(String, nullable=False)
    categories = Column(String, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

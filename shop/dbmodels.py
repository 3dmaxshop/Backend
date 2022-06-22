from db import Base, engine
from sqlalchemy import Column, Integer, String


class Models(Base):
    __tablename__ = 'models'

    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    color = Column(String, unique=True)
    catigories = Column(String, primary_key=True)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

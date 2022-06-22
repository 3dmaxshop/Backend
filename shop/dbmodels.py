from db import Base, engine
from sqlalchemy import Column, Integer, String


class Models(Base):
    __tablename__ = 'models'

    uid = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    color = Column(String, nullable=False)
    catigories = Column(String, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

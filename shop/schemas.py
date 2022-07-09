from pydantic import BaseModel


class Model(BaseModel):
    name: str
    color: str
    uid: int
    category_id: int

    class Config:
        orm_mode = True


class Category(BaseModel):
    name: str
    uid: int

    class Config:
        orm_mode = True

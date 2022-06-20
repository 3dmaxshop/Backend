from pydantic import BaseModel


class Model(BaseModel):
    name: str
    color: str
    uid: int
    catigories: str

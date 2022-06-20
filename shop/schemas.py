from pydantic import BaseModel


class CorrectModel(BaseModel):
    name: str
    color: str
    uid: int
    catigories: str

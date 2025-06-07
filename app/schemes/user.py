from pydantic import BaseModel
from schemes.collection import Collection


class User(BaseModel):
    name: str
    collections: list[Collection] = []

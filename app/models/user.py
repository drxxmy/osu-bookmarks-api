from pydantic import BaseModel
from .collection import Collection


class User(BaseModel):
    name: str
    collections: list[Collection]

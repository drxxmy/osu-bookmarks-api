from pydantic import BaseModel
from models.collection import Collection


class User(BaseModel):
    name: str
    collections: list[Collection]

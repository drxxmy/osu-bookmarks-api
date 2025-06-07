from pydantic import BaseModel, Field
from .collection import Collection


class User(BaseModel):
    name: str
    collections: list[Collection]

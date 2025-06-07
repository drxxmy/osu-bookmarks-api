from pydantic import BaseModel, Field
from .bookmark import Bookmark


class Collection(BaseModel):
    name: str
    bookmarks: list[Bookmark]

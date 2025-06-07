from pydantic import BaseModel
from .beatmap import Beatmap


class Collection(BaseModel):
    name: str
    beatmaps: list[Beatmap]

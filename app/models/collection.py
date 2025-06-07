from pydantic import BaseModel
from models.beatmap import Beatmap


class Collection(BaseModel):
    name: str
    beatmaps: list[Beatmap]

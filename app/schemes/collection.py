from pydantic import BaseModel, Field
from schemes.beatmap import Beatmap
import datetime as dt


class Collection(BaseModel):
    name: str
    beatmaps: list[Beatmap]
    created_at: dt.datetime = Field(default_factory=dt.datetime.now)

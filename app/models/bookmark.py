from pydantic import BaseModel, Field
from .beatmap import Beatmap
import datetime as dt


class Bookmark(BaseModel):
    beatmap: Beatmap
    date_added: dt.datetime = Field(default_factory=dt.datetime.now)

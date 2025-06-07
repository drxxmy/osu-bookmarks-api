from pydantic import BaseModel, Field
from typing import Optional, List
import datetime as dt


class Beatmap(BaseModel):
    map_id: int
    song_name: str
    artist_name: str
    map_creator_name: str
    map_creator_id: int
    tags: Optional[List[str]] = None
    date_added: dt.datetime = Field(default_factory=dt.datetime.now)

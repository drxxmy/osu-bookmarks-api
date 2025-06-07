from pydantic import BaseModel
from typing import Optional, List


class Beatmap(BaseModel):
    map_id: int
    song_name: str
    artist_name: str
    map_creator_name: str
    map_creator_id: int
    tags: Optional[List[str]] = None

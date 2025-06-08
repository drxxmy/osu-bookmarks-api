from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


# Beatmap models
class BeatmapBase(BaseModel):
    id: int
    beatmap_id: int
    song_title: str
    song_artist: str
    mapper_id: int
    mapper_username: str

    class Config:
        from_attributes = True


class BeatmapCreate(BaseModel):
    beatmap_id: int
    song_title: str
    song_artist: str
    mapper_id: int
    mapper_username: str


# Collection models
class CollectionBase(BaseModel):
    id: int
    title: str
    user_id: int
    description: Optional[str]
    created_at: datetime
    modified_at: datetime
    beatmaps: List[BeatmapBase] = []

    class Config:
        from_attributes = True


class CollectionCreate(BaseModel):
    title: str
    description: Optional[str]
    beatmaps: Optional[List[BeatmapCreate]] = []


# User models
class UserBase(BaseModel):
    id: int
    username: str
    created_at: datetime


class UserWithCollections(UserBase):
    collections: List[CollectionBase] = []


# For creating users
class UserCreate(BaseModel):
    username: str


# For deleting users
class UserDelete(BaseModel):
    id: int

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime as dt


class Beatmap(BaseModel):
    map_id: int
    song_name: str
    artist_name: str
    map_creator_name: str
    map_creator_id: int
    tags: list[str] | None


class Bookmark(BaseModel):
    beatmap: Beatmap
    date_added: dt.datetime


class Collection(BaseModel):
    name: str
    bookmarks: list[Bookmark]


class User(BaseModel):
    name: str
    collections: list[Collection]


users: list[User] = []
test_user = User(name="Test", bookmarks=[])
users.append(test_user)

app = FastAPI()


@app.get("/api/v1/users/{user_id}/collections/{collection_id}/bookmarks")
async def list_bookmarks(user_id: int, collection_id: int, limit: int = 25):
    return users[user_id].collections[collection_id].bookmarks[0:limit]


@app.post("/api/v1/users/{user_id}/collections/{collection_id}/bookmarks")
async def create_bookmark(user_id: int, collection_id: int, bookmark: Bookmark):
    users[user_id].collections[collection_id].bookmarks.append(bookmark)
    return users[user_id].collections[collection_id].bookmarks


@app.get("/api/v1/users/{user_id}/collections/{collection_id}/bookmarks/{bookmark_id}")
async def get_bookmark(user_id: int, collection_id: int, bookmark_id: int) -> Bookmark:
    if bookmark_id < len(users[user_id].collections[collection_id].bookmarks):
        return users[user_id].collections[collection_id].bookmarks[bookmark_id]
    else:
        raise HTTPException(
            404,
            f"Cannot use id: '{bookmark_id}' since it is out of range!",
        )

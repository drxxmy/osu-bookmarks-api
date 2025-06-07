from fastapi import FastAPI, HTTPException, status
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
    try:
        user = users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    try:
        collection = user.collections[collection_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Collection with id {collection_id} not found for user {user_id}",
        )

    return collection.bookmarks[:limit]


@app.post(
    "/api/v1/users/{user_id}/collections/{collection_id}/bookmarks",
    status_code=status.HTTP_201_CREATED,
)
async def create_bookmark(user_id: int, collection_id: int, bookmark: Bookmark):
    try:
        user = users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    try:
        collection = user.collections[collection_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Collection with id {collection_id} not found for user {user_id}",
        )

    collection.bookmarks.append(bookmark)
    return bookmark


@app.get("/api/v1/users/{user_id}/collections/{collection_id}/bookmarks/{bookmark_id}")
async def get_bookmark(user_id: int, collection_id: int, bookmark_id: int) -> Bookmark:
    try:
        user = users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    try:
        collection = user.collections[collection_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Collection with id {collection_id} not found for user {user_id}",
        )

    return collection.bookmarks[bookmark_id]

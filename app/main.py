from fastapi import FastAPI, HTTPException, status
from models import beatmap, bookmark, collection, user
import datetime as dt


users: list[user.User] = []
test_user = user.User(name="Test", collections=[])
users.append(test_user)

app = FastAPI()


@app.get(
    "/api/v1/users/{user_id}/collections/{collection_id}/bookmarks",
    response_model=list[bookmark.Bookmark],
)
async def list_bookmarks(
    user_id: int, collection_id: int, limit: int = 25
) -> list[bookmark.Bookmark]:
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
    response_model=bookmark.Bookmark,
)
async def create_bookmark(
    user_id: int, collection_id: int, bookmark: bookmark.Bookmark
) -> bookmark.Bookmark:
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


@app.get(
    "/api/v1/users/{user_id}/collections/{collection_id}/bookmarks/{bookmark_id}",
    response_model=bookmark.Bookmark,
)
async def get_bookmark(
    user_id: int, collection_id: int, bookmark_id: int
) -> bookmark.Bookmark:
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

from fastapi import HTTPException, status
from models.user import User
from models.beatmap import Beatmap
from models.collection import Collection

# b = Bookmark("")
# c = Collection(name="cool maps", bookmarks=)
users: list[User] = []
test_user = User(name="Test", collections=[])
users.append(test_user)


def list_beatmaps(user_id: int, collection_id: int, limit: int = 25) -> list[Beatmap]:
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

    return collection.beatmaps[:limit]


def add_beatmap(user_id: int, collection_id: int, beatmap: Beatmap) -> Beatmap:
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

    collection.beatmaps.append(beatmap)
    return beatmap


def get_beatmap(user_id: int, collection_id: int, beatmap_id: int) -> Beatmap:
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

    return collection.beatmaps[beatmap_id]

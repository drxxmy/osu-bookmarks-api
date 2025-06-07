from fastapi import HTTPException, status
from schemes.user import User
from schemes.collection import Collection
from tests.test_data import create_test_data

# Initialize with test data
users: list[User] = create_test_data()


def list_collections(user_id: int, limit: int = 25) -> list[Collection]:
    try:
        user = users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user.collections[:limit]


def get_collection(user_id: int, collection_id: int) -> Collection:
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

    return collection

from fastapi import HTTPException, status
from schemes.user import User
from schemes.collection import Collection
from tests.test_data import create_test_data

# Initialize with test data
users: list[User] = create_test_data()


def list_collections(user_id: int, limit: int = 25) -> list[Collection]:
    """List collections from a user.

    This function looks up collections from a specified user and returns a list of them.
    It performs a check to ensure the user exist before returning the list.

    Args:
        user_id: The ID of the user who owns the collections.
        limit: Limit of the returned collections.

    Returns:
        list[Collection]: The requested list of collections.

    Raises:
        HTTPException: 404 error if either:
            - The user with the specified ID doesn't exist
    """
    try:
        user = users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user.collections[:limit]


def get_collection(user_id: int, collection_id: int) -> Collection:
    """Retrieve a specific collection from a user.

    This function looks up a collection by its ID within a specified collection belonging
    to a particular user. It performs several checks to ensure the user and collection
    exist before returning the collection.

    Args:
        user_id: The ID of the user who owns the collection.
        collection_id: The ID of the collection.

    Returns:
        Collection: The requested collection object if found.

    Raises:
        HTTPException: 404 error if either:
            - The user with the specified ID doesn't exist
            - The collection with the specified ID doesn't exist for the user
    """
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

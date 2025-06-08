from fastapi import HTTPException, status
from schemes.user import User
from schemes.beatmap import Beatmap
from tests.test_data import create_test_data

# Initialize with test data
users: list[User] = create_test_data()


def list_beatmaps(user_id: int, collection_id: int, limit: int = 25) -> list[Beatmap]:
    """List beatmaps from a user's collection.

    This function returns a list of beatmaps from a specified collection belonging
    to a particular user. It performs several checks to ensure the user and collection
    exist before returning the list of beatmaps.

    Args:
        user_id: The ID of the user who owns the collection.
        collection_id: The ID of the collection that should contain the beatmap.
        limit: Limit the amount of returned beatmaps.

    Returns:
        list[Beatmap]: List of the beatmaps if found.

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

    return collection.beatmaps[:limit]


def add_beatmap(user_id: int, collection_id: int, beatmap: Beatmap) -> Beatmap:
    """Add a specific beatmap to a user's collection.

    This function adds a beatmap object to a specified collection belonging
    to a particular user. It performs several checks to ensure the user and collection
    exist before returning the beatmap.

    Args:
        user_id: The ID of the user who owns the collection.
        collection_id: The ID of the collection that should contain the beatmap.
        beatmap_id: The ID of the beatmap to add.

    Returns:
        Beatmap: The added beatmap object.

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

    collection.beatmaps.append(beatmap)
    return beatmap


def get_beatmap(user_id: int, collection_id: int, beatmap_id: int) -> Beatmap:
    """Retrieve a specific beatmap from a user's collection.

    This function looks up a beatmap by its ID within a specified collection belonging
    to a particular user. It performs several checks to ensure the user, collection,
    and beatmap exist before returning the beatmap.

    Args:
        user_id: The ID of the user who owns the collection.
        collection_id: The ID of the collection containing the beatmap.
        beatmap_id: The ID of the beatmap to retrieve.

    Returns:
        Beatmap: The requested beatmap object if found.

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

    return collection.beatmaps[beatmap_id]

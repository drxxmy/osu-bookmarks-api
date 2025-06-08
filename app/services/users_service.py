from fastapi import HTTPException, status
from schemes.user import User
from tests.test_data import create_test_data

# Initialize with test data
users: list[User] = create_test_data()


def list_users(limit: int = 25) -> list[User]:
    """Retrieve a list of users.

    This function returns a list of users within the specified limit.

    Args:
        limit: The limit of users returned in a list.

    Returns:
        list[User]: The requested list of user objects.
    """
    return users[:limit]


def get_user(user_id: int) -> User:
    """Retrieve a specific user.

    This function looks up a user by their ID. It performs a check to ensure the user
    exist before returning the user.

    Args:
        user_id: The ID of the user who owns the collection.

    Returns:
        User: The requested user object if found.

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

    return user

from fastapi import HTTPException, status
from schemes.user import User
from tests.test_data import create_test_data

# Initialize with test data
users: list[User] = create_test_data()


def list_users(limit: int = 25) -> list[User]:
    return users[:limit]


def get_user(user_id: int) -> User:
    try:
        user = users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user

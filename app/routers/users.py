from fastapi import APIRouter
from models.user import User
from services import users_service

router = APIRouter(prefix="/api/v1", tags=["users"])


@router.get(
    "/users",
    response_model=list[User],
)
async def list_users(limit: int = 25) -> list[User]:
    return users_service.list_users(limit)


@router.get(
    "/users/{user_id}",
    response_model=User,
)
async def get_user(user_id: int) -> User:
    return users_service.get_user(user_id)

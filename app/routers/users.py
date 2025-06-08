from database.database import get_db
from database.models import UserBase, UserCreate, UserDelete
from database.schemes import User
from fastapi import APIRouter, Depends, status
from services import users_service
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/v1", tags=["users"])


@router.post(
    "/users/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserCreate,
)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return users_service.create_user(db, user)


@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return users_service.delete_user(db, user_id)


@router.get(
    "/users",
    response_model=list[UserBase],
)
async def list_users(
    skip: int = 0, limit: int = 25, db: Session = Depends(get_db)
) -> list[User]:
    return users_service.list_users(db, skip, limit)


@router.get(
    "/users/{user_id}",
    response_model=UserBase,
)
async def get_user(user_id: int, db: Session = Depends(get_db)) -> User:
    return users_service.get_user(db, user_id)

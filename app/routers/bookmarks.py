from fastapi import APIRouter, status
from models.bookmark import Bookmark
from services import bookmarks_service

router = APIRouter(
    prefix="/api/v1/users/{user_id}/collections/{collection_id}", tags=["bookmarks"]
)


@router.get(
    "/bookmarks",
    response_model=list[Bookmark],
)
async def list_bookmarks(
    user_id: int, collection_id: int, limit: int = 25
) -> list[Bookmark]:
    return bookmarks_service.list_bookmarks(user_id, collection_id, limit)


@router.post(
    "/bookmarks",
    status_code=status.HTTP_201_CREATED,
    response_model=Bookmark,
)
async def create_bookmark(user_id: int, collection_id: int, bookmark: Bookmark):
    return bookmarks_service.create_bookmark(user_id, collection_id, bookmark)


@router.get(
    "/bookmarks/{bookmark_id}",
    response_model=Bookmark,
)
async def get_bookmark(user_id: int, collection_id: int, bookmark_id: int) -> Bookmark:
    return bookmarks_service.get_bookmark(user_id, collection_id, bookmark_id)

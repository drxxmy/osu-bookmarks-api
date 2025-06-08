from database.database import get_db
from database.models import CollectionBase, CollectionCreate
from database.schemes import Collection
from fastapi import APIRouter, Depends, status
from services import collections_service
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/v1/users/{user_id}", tags=["collections"])


@router.post(
    "/collections",
    status_code=status.HTTP_201_CREATED,
    response_model=CollectionCreate,
)
async def create_collection(
    user_id: int, collection: CollectionCreate, db: Session = Depends(get_db)
):
    return collections_service.create_collection(db, collection)


@router.delete(
    "/collections/{collection_id}",
    status_code=status.HTTP_200_OK,
)
async def delete_collection(
    collection_id: int, user_id: int, db: Session = Depends(get_db)
):
    return collections_service.delete_collection(db, collection_id, user_id)


@router.get(
    "/collections",
    response_model=list[CollectionBase],
)
async def list_collections(
    user_id: int, skip: int = 0, limit: int = 25, db: Session = Depends(get_db)
) -> list[Collection]:
    return collections_service.list_collections(db, user_id, skip, limit)


@router.get(
    "/collections/{collection_id}",
    response_model=CollectionBase,
)
async def get_collection(
    user_id: int, collection_id: int, db: Session = Depends(get_db)
) -> Collection:
    return collections_service.get_collection(db, user_id, collection_id)

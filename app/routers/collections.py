from fastapi import APIRouter
from models.collection import Collection
from services import collections_service

router = APIRouter(prefix="/api/v1/users/{user_id}", tags=["collections"])


@router.get(
    "/collections",
    response_model=list[Collection],
)
async def list_collections(user_id: int) -> list[Collection]:
    return collections_service.list_collections(user_id)


@router.get(
    "/collections/{collection_id}",
    response_model=Collection,
)
async def get_collection(user_id: int, collection_id: int) -> Collection:
    return collections_service.get_collection(user_id, collection_id)

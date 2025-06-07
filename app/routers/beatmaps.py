from fastapi import APIRouter, status
from models.beatmap import Beatmap
from services import beatmaps_service

router = APIRouter(
    prefix="/api/v1/users/{user_id}/collections/{collection_id}", tags=["beatmaps"]
)


@router.get(
    "/beatmaps",
    response_model=list[Beatmap],
)
async def list_beatmaps(
    user_id: int, collection_id: int, limit: int = 25
) -> list[Beatmap]:
    return beatmaps_service.list_beatmaps(user_id, collection_id, limit)


@router.post(
    "/beatmaps",
    status_code=status.HTTP_201_CREATED,
    response_model=Beatmap,
)
async def add_beatmap(user_id: int, collection_id: int, beatmap: Beatmap):
    return beatmaps_service.add_beatmap(user_id, collection_id, beatmap)


@router.get(
    "/beatmaps/{beatmap_id}",
    response_model=Beatmap,
)
async def get_beatmap(user_id: int, collection_id: int, beatmap_id: int) -> Beatmap:
    return beatmaps_service.get_beatmap(user_id, collection_id, beatmap_id)

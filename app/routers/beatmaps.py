from database.database import get_db
from database.models import BeatmapBase, BeatmapCreate
from database.schemes import Beatmap
from fastapi import APIRouter, Depends, status
from services import beatmaps_service
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/api/v1/users/{user_id}/collections/{collection_id}", tags=["beatmaps"]
)


@router.get(
    "/beatmaps",
    response_model=list[BeatmapBase],
)
async def list_beatmaps(
    user_id: int, collection_id: int, limit: int = 25, db: Session = Depends(get_db)
) -> list[Beatmap]:
    return beatmaps_service.list_beatmaps(db, user_id, collection_id, limit)


@router.post(
    "/beatmaps",
    status_code=status.HTTP_201_CREATED,
    response_model=BeatmapCreate,
)
async def add_beatmap(
    user_id: int,
    collection_id: int,
    beatmap_id: int,
    db: Session = Depends(get_db),
):
    return beatmaps_service.add_beatmap(db, user_id, collection_id, beatmap_id)


@router.get(
    "/beatmaps/{beatmap_id}",
    response_model=BeatmapBase,
)
async def get_beatmap(
    user_id: int, collection_id: int, beatmap_id: int, db: Session = Depends(get_db)
) -> Beatmap:
    return beatmaps_service.get_beatmap(db, user_id, collection_id, beatmap_id)

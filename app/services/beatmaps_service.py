from database.schemes import Beatmap
from services.collections_service import get_collection
from sqlalchemy.orm import Session
from utils import osu_api


def list_beatmaps(
    db: Session, user_id: int, collection_id: int, limit: int = 25
) -> list[Beatmap]:
    collection = get_collection(db, user_id, collection_id)

    if not collection:
        return []

    return collection.beatmaps[:limit]


def add_beatmap(
    db: Session, user_id: int, collection_id: int, beatmap_id: int
) -> Beatmap:
    # Fetch the collection
    collection = get_collection(db, user_id, collection_id)

    beatmap = osu_api.api.beatmapset(beatmap_id)

    # Create ORM instance from Pydantic data
    new_beatmap = Beatmap(
        beatmap_id=beatmap.id,
        song_title=beatmap.title_unicode,
        song_artist=beatmap.artist_unicode,
        mapper_id=beatmap.user_id,
        mapper_username=beatmap.user().username,
    )

    # Append the ORM object to the collection's relationship
    collection.beatmaps.append(new_beatmap)

    # Commit the session
    db.add(new_beatmap)
    db.commit()
    db.refresh(new_beatmap)

    return new_beatmap


def get_beatmap(
    db: Session, user_id: int, collection_id: int, beatmap_id: int
) -> Beatmap:
    collection = get_collection(db, user_id, collection_id)

    return collection.beatmaps[beatmap_id]

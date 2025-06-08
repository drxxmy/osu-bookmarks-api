from database.models import BeatmapCreate
from database.schemes import Beatmap
from services.collections_service import get_collection
from services.users_service import get_user
from sqlalchemy.orm import Session


def list_beatmaps(
    db: Session, user_id: int, collection_id: int, limit: int = 25
) -> list[Beatmap]:
    collection = get_collection(db, user_id, collection_id)

    if not collection:
        return []

    # Access related beatmaps via relationship
    return collection.beatmaps[:limit]
    # user_id = Column(Integer, ForeignKey("users.id"))
    # collection = get_collection(db, user_id, collection_id)

    # beatmaps = (
    #     db.query(Beatmap)
    #     .filter(Beatmap.collection_id == collection.id)
    #     .limit(limit)
    #     .all()
    # )

    # return beatmaps


def add_beatmap(
    db: Session, user_id: int, collection_id: int, beatmap: BeatmapCreate
) -> Beatmap:
    # Fetch the collection
    collection = get_collection(db, user_id, collection_id)

    # Create ORM instance from Pydantic data
    new_beatmap = Beatmap(
        beatmap_id=beatmap.beatmap_id,
        song_title=beatmap.song_title,
        song_artist=beatmap.song_artist,
        mapper_id=beatmap.mapper_id,
        mapper_username=beatmap.mapper_username,
    )

    # Append the ORM object to the collection's relationship
    collection.beatmaps.append(new_beatmap)

    # Commit the session
    db.add(new_beatmap)
    db.commit()
    db.refresh(new_beatmap)

    return new_beatmap
    collection = get_collection(db, user_id, collection_id)

    collection.beatmaps.append(beatmap)
    return beatmap


def get_beatmap(
    db: Session, user_id: int, collection_id: int, beatmap_id: int
) -> Beatmap:
    collection = get_collection(db, user_id, collection_id)

    return collection.beatmaps[beatmap_id]

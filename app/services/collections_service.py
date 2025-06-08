from database.models import CollectionCreate
from database.schemes import Collection
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def create_collection(
    db: Session, user_id: int, collection: CollectionCreate
) -> Collection:
    db_collection = Collection(user_id=user_id, **collection.model_dump())
    db.add(db_collection)
    db.commit()

    return db_collection


def delete_collection(db: Session, collection_id: int, user_id: int):
    db_collection = (
        db.query(Collection)
        .filter(Collection.id == collection_id, Collection.user_id == user_id)
        .first()
    )

    if not db_collection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Collection with id {collection_id} not found for user {user_id}",
        )

    db.delete(db_collection)
    db.commit()


def list_collections(
    db: Session, user_id: int, skip: int = 0, limit: int = 25
) -> list[Collection]:
    collections = (
        db.query(Collection)
        .filter(Collection.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

    return collections


def get_collection(db: Session, user_id: int, collection_id: int) -> Collection:
    collection = (
        db.query(Collection)
        .filter(Collection.id == collection_id, Collection.user_id == user_id)
        .first()
    )

    if not collection:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Collection with id {collection_id} not found for user {user_id}",
        )

    return collection

from database.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table, func
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    created_at = Column(DateTime, default=func.now())

    # Relationship to collections
    collections = relationship("Collection", back_populates="user")


# An association table for many-to-many
collection_beatmap_association = Table(
    "collection_beatmap",
    Base.metadata,
    Column("collection_id", Integer, ForeignKey("collections.id"), primary_key=True),
    Column("beatmap_id", Integer, ForeignKey("beatmaps.id"), primary_key=True),
)


class Collection(Base):
    __tablename__ = "collections"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(50))
    description = Column(String(100))
    created_at = Column(DateTime, default=func.now())
    modified_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationship back to User
    user = relationship("User", back_populates="collections")

    # Relationship to beatmaps via the association table
    beatmaps = relationship(
        "Beatmap",
        secondary=collection_beatmap_association,
        back_populates="collections",
    )


class Beatmap(Base):
    __tablename__ = "beatmaps"

    id = Column(Integer, primary_key=True, index=True)
    beatmap_id = Column(Integer)
    song_title = Column(String(100))
    song_artist = Column(String(50))
    mapper_id = Column(Integer)
    mapper_username = Column(String(50))

    # Relationship back to collections
    collections = relationship(
        "Collection",
        secondary=collection_beatmap_association,
        back_populates="beatmaps",
    )

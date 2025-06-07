from fastapi import HTTPException, status
from models.user import User
from models.beatmap import Beatmap
from models.collection import Collection

x = Beatmap(
    map_id=1034179,
    song_name="Yuuga ni Sakase, Sumizome no Sakura ~ The Harm of Coming into Existence",
    artist_name="Demetori",
    map_creator_name="jonathanlfj",
    map_creator_id=270377,
)
y = Beatmap(
    map_id=2069184,
    song_name="Imperfect Cherry Blossom",
    artist_name="Adust Rain",
    map_creator_name="Orkay",
    map_creator_id=9321674,
)
c = Collection(name="cool maps", beatmaps=[x, y])
a = Collection(name="another cool maps", beatmaps=[x, y])
users: list[User] = []
test_user = User(name="Test", collections=[a, c])
users.append(test_user)


def list_collections(user_id: int, limit: int = 25) -> list[Collection]:
    try:
        user = users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user.collections[:limit]


def get_collection(user_id: int, collection_id: int) -> Collection:
    try:
        user = users[user_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    try:
        collection = user.collections[collection_id]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Collection with id {collection_id} not found for user {user_id}",
        )

    return collection

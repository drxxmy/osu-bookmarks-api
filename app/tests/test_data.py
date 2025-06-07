from schemes.beatmap import Beatmap
from schemes.collection import Collection
from schemes.user import User


def create_test_data():
    """Returns a list of test users with collections and beatmaps"""
    first_user = User(name="First user")

    first_map = Beatmap(
        map_id=1034179,
        song_name="Yuuga ni Sakase, Sumizome no Sakura ~ The Harm of Coming into Existence",
        artist_name="Demetori",
        map_creator_name="jonathanlfj",
        map_creator_id=270377,
    )
    second_map = Beatmap(
        map_id=2069184,
        song_name="Imperfect Cherry Blossom",
        artist_name="Adust Rain",
        map_creator_name="Orkay",
        map_creator_id=9321674,
    )

    first_collection = Collection(name="cool maps", beatmaps=[first_map, second_map])
    second_user = User(name="Second user", collections=[first_collection])
    return [first_user, second_user]

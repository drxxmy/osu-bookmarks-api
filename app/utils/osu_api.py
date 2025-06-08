import os

from dotenv import load_dotenv
from ossapi import Ossapi

load_dotenv()

client_id = int(os.environ["OSU_CLIENT_ID"])
client_secret = os.environ["OSU_CLIENT_SECRET"]

api = Ossapi(client_id, client_secret)

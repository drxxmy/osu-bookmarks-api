from fastapi import FastAPI
from routers import beatmaps, collections, users


app = FastAPI()

app.include_router(beatmaps.router)
app.include_router(collections.router)
app.include_router(users.router)

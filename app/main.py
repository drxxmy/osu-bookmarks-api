from fastapi import FastAPI
from routers import beatmaps, collections, users


app = FastAPI(
    title="osu!bookmarks API",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
)

app.include_router(beatmaps.router)
app.include_router(collections.router)
app.include_router(users.router)

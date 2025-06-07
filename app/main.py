from fastapi import FastAPI
from routers import beatmaps


app = FastAPI()

app.include_router(beatmaps.router)

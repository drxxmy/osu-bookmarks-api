from fastapi import FastAPI
from routers import bookmarks


app = FastAPI()

app.include_router(bookmarks.router)

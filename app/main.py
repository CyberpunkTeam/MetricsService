from fastapi import FastAPI
from .routers import tracks, state


app = FastAPI()


app.include_router(tracks.router)
app.include_router(state.router)

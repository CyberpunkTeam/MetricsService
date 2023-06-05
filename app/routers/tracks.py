from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.tracks_controller import TracksController
from app.models.tracks import Tracks
from app.repositories.tracks_repository import TracksRepository

router = APIRouter()

# Repository
tracks_repository = TracksRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post("/tracks/", tags=["tracks"], response_model=List[Tracks], status_code=201)
async def create_track(track: List[Tracks]):
    return TracksController.post(tracks_repository, track)


@router.get("/tracks/", tags=["tracks"], response_model=List[Tracks])
async def list_tracks():
    return TracksController.get(tracks_repository)


@router.get("/metrics/", tags=["tracks"], response_model=List[Tracks])
async def get_metrics():
    return TracksController.get_metrics(tracks_repository)

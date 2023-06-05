from typing import List

from fastapi import HTTPException
from app.models.tracks import Tracks


class TracksController:
    @staticmethod
    def post(repository, tracks: List[Tracks]):
        ok = repository.insert_many(tracks)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return tracks

    @staticmethod
    def get(repository):
        result = repository.get()
        return result

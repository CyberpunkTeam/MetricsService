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

    @staticmethod
    def get_metrics(repository):
        result = repository.get(path="/session")

        session_created = {}
        for track in result:
            session_created[track.created_date] = (
                session_created.get(track.created_date, 0) + 1
            )

        result = {
            "session_created": {
                "labels": list(session_created.keys()),
                "values": list(session_created.values()),
            }
        }
        return result

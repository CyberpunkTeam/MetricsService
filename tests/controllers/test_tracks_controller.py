from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.controllers.tracks_controller import TracksController
from app.models.tracks import Tracks


def test_get_all_tracks():
    repository = Mock()
    repository.get.return_value = [
        Tracks(
            uid="111",
            path="/session",
            created_date="2023-02-03",
        ),
    ]
    result = TracksController.get(repository)
    assert len(result) == 1


def test_create_track():
    repository = Mock()
    repository.insert_many.return_value = True
    track = Tracks(
        uid="111",
        path="/session",
        created_date="2023-02-03",
    )
    result = TracksController.post(repository, [track])
    assert result == [track]


def test_error_create_track():
    repository = Mock()
    repository.insert_many.return_value = False
    tracks = [Tracks(uid="111", path="/session", created_date="2023-02-03")]

    with pytest.raises(HTTPException):
        TracksController.post(repository, tracks)

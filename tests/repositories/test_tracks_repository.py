import mongomock

from app import config
from app.models.tracks import Tracks
from app.repositories.tracks_repository import TracksRepository


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_save_track():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = TracksRepository(url, db_name)

    user = Tracks(uid="111", path="/session", created_date="2023-02-03")

    ok = repository.insert(user)

    assert ok


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_user():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = TracksRepository(url, db_name)

    track = Tracks(uid="111", path="/session", created_date="2023-02-03")

    ok = repository.insert(track)

    assert ok

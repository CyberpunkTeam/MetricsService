from app.models.tracks import Tracks


def test_create_track():
    track = Tracks(uid="111", path="/session", created_date="2023-02-03")
    assert track.uid == "111"
    assert track.path == "/session"
    assert track.created_date == "2023-02-03"

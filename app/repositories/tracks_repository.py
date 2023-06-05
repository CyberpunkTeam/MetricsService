from typing import List

from cpunk_mongo.db import DataBase

from app.models.tracks import Tracks


class TracksRepository(DataBase):
    COLLECTION_NAME = "tracks"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, path=None):
        filters = {}
        if path:
            filters["path"] = path
        return self.filter(self.COLLECTION_NAME, filters, output_model=Tracks)

    def insert(self, track: Tracks):
        return self.save(self.COLLECTION_NAME, track)

    def insert_many(self, tracks: List[Tracks]):
        return self.save_many(self.COLLECTION_NAME, tracks)

    @staticmethod
    def create_repository(url, database_name):
        return TracksRepository(url, database_name)

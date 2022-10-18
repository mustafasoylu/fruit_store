from datetime import datetime
from src.database.entity import Collection
import pymongo
from enum import Enum
from typing import Optional


class IndexType(Enum):
    ASCENDING = pymongo.ASCENDING
    DESCENDING = pymongo.DESCENDING


class BucketCollection(Collection):
    def __init__(self, db, collection_name: str):
        super().__init__(db, collection_name)
        self.set_index(index_name="timestamp", index_type=IndexType.ASCENDING)

    def set_index(self, index_name: str, index_type: IndexType) -> None:
        self.collection.create_index([(index_name, index_type.value)])

    def insert(self, row: dict) -> bool:
        self.collection.insert_one(row)
        return True

    def find(self, timestamp: datetime) -> Optional[dict]:
        cursor = self._get_cursor(timestamp)

        row = next(cursor, None)
        return row

    def _get_cursor(self, timestamp: datetime):
        return (
            self.collection.find({"timestamp": {"$lte": timestamp}}, {"_id": 0})
            .sort("timestamp", -1)
            .limit(1)
        )

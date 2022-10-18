from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.database.bucket import BucketCollection, IndexType
from src.database.mongo import MongoDB


class TestBucketCollection(TestCase):
    USER = "user"
    PASSWORD = "password"
    HOST = "host"
    PORT = 27017
    CONNECTION_STRING = f"mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}"
    DB_NAME = "test_db"
    COLLECTION_NAME = "test_collection"
    TIMEOUT = 1000
    ROW = {"timestamp": 1, "fruits": {"apple": 1, "banana": 2}}
    TIMESTAMP = 1234567890

    def setUp(self):
        db = MagicMock()
        self.bucket = BucketCollection(db, self.COLLECTION_NAME)

    def test_set_index(self):
        # arrange
        self.bucket.collection = MagicMock()

        # act
        self.bucket.set_index("timestamp", IndexType.ASCENDING)

        # assert
        self.bucket.collection.create_index.assert_called_once_with([("timestamp", 1)])

    def test_insert(self):
        # arrange
        self.bucket.collection = MagicMock()

        # act
        self.bucket.insert(self.ROW)

        # assert
        self.bucket.collection.insert_one.assert_called_once_with(self.ROW)

    def test_find(self):
        # arrange
        self.bucket.collection = MagicMock()

        # act
        self.bucket.find(self.TIMESTAMP)

        # assert
        self.bucket.collection.find.assert_called_once_with(
            {"timestamp": {"$lte": self.TIMESTAMP}}, {"_id": 0}
        )

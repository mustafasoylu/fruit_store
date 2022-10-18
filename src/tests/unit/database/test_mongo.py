import unittest
from unittest.mock import patch, MagicMock
from src.database.mongo import MongoDB, get_mongo_connection_string


class TestMongo(unittest.TestCase):
    USER = "user"
    PASSWORD = "password"
    HOST = "host"
    PORT = 27017
    CONNECTION_STRING = f"mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}"
    DB_NAME = "test_db"
    COLLECTION_NAME = "test_collection"
    TIMEOUT = 1000

    def setUp(self):
        self.client = MongoDB(self.CONNECTION_STRING, self.DB_NAME, self.TIMEOUT)

    # Test get_mongo_connection_string
    def test_get_mongo_connection_string(self):
        # arrange
        # act
        result = get_mongo_connection_string(
            self.USER, self.PASSWORD, self.HOST, self.PORT
        )

        # assert
        self.assertEqual(result, self.CONNECTION_STRING)

    # test mongodb connect with mock instance
    @patch("src.database.mongo.MongoClient")
    def test_connect(self, mock_client):
        # arrange
        mock_client.return_value = MagicMock()

        # act
        self.client.connect()

        # assert
        mock_client.assert_called_once_with(
            self.CONNECTION_STRING, serverSelectionTimeoutMS=self.TIMEOUT
        )

        mock_client.return_value.__getitem__.assert_called_once_with(self.DB_NAME)

    # test mongodb connect with mock instance
    def test_create_collection(self):
        # arrange
        self.client.db = MagicMock()

        # act
        self.client.create_collection(self.COLLECTION_NAME)

        # assert
        self.client.db.__getitem__.assert_called_once_with(self.COLLECTION_NAME)


if __name__ == "__main__":
    unittest.main()

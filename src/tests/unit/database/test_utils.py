import unittest
from unittest.mock import patch, MagicMock
from src.database.utils import get_connection_string, get_db, get_bucket
from src.database.mongo import MongoDB
from src.database.bucket import BucketCollection


class DBUtils(unittest.TestCase):
    DB_TYPE = "MONGO"
    INVALID_DB_TYPE = "invalid"
    USER = "user"
    PASSWORD = "password"
    HOST = "host"
    PORT = 27017
    CONNECTION_STRING = f"mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}"
    DB_NAME = "test_db"
    COLLECTION_NAME = "test_collection"
    TIMEOUT = 1000

    def test_get_connection_string_invalid(self):
        # Test with invalid db_type
        with self.assertRaises(ValueError):
            get_connection_string(
                self.INVALID_DB_TYPE, self.USER, self.PASSWORD, self.HOST, self.PORT
            )

    def test_get_connection_string(self):
        # Test with valid db_type
        self.assertEqual(
            get_connection_string(
                self.DB_TYPE, self.USER, self.PASSWORD, self.HOST, self.PORT
            ),
            self.CONNECTION_STRING,
        )

    def test_get_db(self):
        # arrange

        # act
        db = get_db(
            self.DB_TYPE,
            self.USER,
            self.PASSWORD,
            self.HOST,
            self.PORT,
            self.DB_NAME,
            self.TIMEOUT,
        )

        # assert
        self.assertIsInstance(
            db,
            MongoDB,
        )

    @patch("src.database.utils.MongoDB")
    def test_get_db_connect(self, mock_db):
        # arrange
        mock_db.return_value = MagicMock()

        # act
        get_db(
            self.DB_TYPE,
            self.USER,
            self.PASSWORD,
            self.HOST,
            self.PORT,
            self.DB_NAME,
            self.TIMEOUT,
        )
        # assert
        mock_db.assert_called_once()
        mock_db.return_value.connect.assert_called_once()

    @patch("src.database.utils.get_db")
    def test_get_bucket(self, get_db_mock):
        # arrange
        get_db_mock.return_value = MagicMock()

        # act
        bucket = get_bucket(
            self.DB_TYPE,
            self.USER,
            self.PASSWORD,
            self.HOST,
            self.PORT,
            self.DB_NAME,
            self.TIMEOUT,
            self.COLLECTION_NAME,
        )

        # assert
        self.assertIsInstance(
            bucket,
            BucketCollection,
        )


if __name__ == "__main__":
    unittest.main()

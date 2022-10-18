import unittest
from unittest.mock import MagicMock, patch, Mock
from src.services.bucket import to_datetime, BucketService
from datetime import datetime
from src.routes.dto.bucket import PostRequest


class TestBucket(unittest.TestCase):
    DATETIME_INT = 1610000000
    DATETIME_INT_DT = datetime.fromtimestamp(DATETIME_INT)
    DATETIME_FLOAT = 1610023000.655
    DATETIME_FLOAT_DT = datetime.fromtimestamp(DATETIME_FLOAT)

    def test_to_datetime_int(self):
        self.assertEqual(to_datetime(self.DATETIME_INT), self.DATETIME_INT_DT)

    def test_to_datetime_float(self):
        self.assertEqual(to_datetime(self.DATETIME_FLOAT), self.DATETIME_FLOAT_DT)

    @patch("src.services.bucket.datetime")
    def test_datetime_none(self, mock_datetime):
        # arrange
        mock_datetime.now = MagicMock()

        # act
        to_datetime()

        # assert
        mock_datetime.now.assert_called_once()

    def test_add_row(self):
        # arrange
        mock_collection = Mock()
        mock_collection.find = MagicMock()
        mock_collection.find.return_value = None
        mock_collection.insert = MagicMock()
        bucket_service = BucketService(mock_collection)
        row = PostRequest(fruits={"apple": 1, "banana": 2})

        # act
        bucket_service.add_row(row)

        # assert
        mock_collection.find.assert_called_once()
        mock_collection.insert.assert_called_once()

    @patch("src.services.bucket.to_datetime")
    def test_find(self, mock_func):
        # arrange
        mock_collection = Mock()
        mock_collection.find = MagicMock()
        mock_collection.find.return_value = None
        bucket_service = BucketService(mock_collection)

        mock_func.return_value = self.DATETIME_INT_DT

        # act
        bucket_service.find(self.DATETIME_INT)

        # assert
        mock_func.assert_called_once_with(self.DATETIME_INT)
        mock_collection.find.assert_called_once_with(self.DATETIME_INT_DT)

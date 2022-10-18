from datetime import datetime
from typing import Union

from src.database.utils import get_bucket
from src.database.entity import Collection
from .validators import validate_fruit_count
from src.utils.log import get_logger


def to_datetime(timestamp: Union[int, float] = None) -> datetime:
    if timestamp:
        return datetime.fromtimestamp(timestamp)
    else:
        return datetime.now()


class BucketService:
    def __init__(self, collection: Collection):
        self.collection = collection
        self.logger = get_logger(self.__class__.__name__)

    def add_row(self, post_request) -> bool:
        self.logger.debug(f"Updating the last row with: {post_request}")

        # get the last row
        now = datetime.now()
        last_row = self.collection.find(now)

        # create a new row from an empty post request
        new_row = {"fruits": {}}
        new_row["timestamp"] = now
        for fruit in post_request.fruits:
            # fruit count
            count = post_request.fruits[fruit]
            if last_row:
                if fruit in last_row["fruits"]:
                    count += last_row["fruits"][fruit]

            validate_fruit_count(fruit, count)

            new_row["fruits"][fruit] = count

        # add the new row
        self.collection.insert(new_row)
        self.logger.debug(f"Added row: {new_row}")
        return True

    def find(self, timestamp: Union[int, float] = None) -> bool:
        self.logger.debug(f"Finding row: {timestamp}")
        date_time = to_datetime(timestamp)
        row = self.collection.find(date_time)

        if row:
            self.logger.debug(f"Found row: {row}")
        else:
            self.logger.debug(f"Found no row, returning empty response")
        return row


def get_bucket_service() -> BucketService:
    return BucketService(collection=get_bucket())

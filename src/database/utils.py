from src.database.mongo import MongoDB, get_mongo_connection_string
from src.database.bucket import BucketCollection
from enum import Enum, auto
from src.common.constants import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
    DB_TYPE,
    DB_TIMEOUT,
    DB_COLLECTION_NAME,
)


class DatabaseType(Enum):
    MONGO = auto()


def get_connection_string(db_type, db_user, db_password, db_host, db_port) -> str:
    try:
        db_type = DatabaseType[db_type.upper()]
    except KeyError:
        raise ValueError(f"Invalid db_type: {db_type}")

    if db_type == DatabaseType.MONGO:
        return get_mongo_connection_string(db_user, db_password, db_host, db_port)
    else:
        raise NotImplementedError()


def get_db(
    db_type, db_user, db_password, db_host, db_port, db_name, db_timeout
) -> MongoDB:
    connection_string = get_connection_string(
        db_type, db_user, db_password, db_host, db_port
    )
    db = MongoDB(connection_string, db_name, db_timeout)
    db.connect()
    return db


def get_bucket(
    db_type=DB_TYPE,
    db_user=DB_USER,
    db_password=DB_PASSWORD,
    db_host=DB_HOST,
    db_port=DB_PORT,
    db_name=DB_NAME,
    db_timeout=DB_TIMEOUT,
    collection_name=DB_COLLECTION_NAME,
) -> BucketCollection:
    db = get_db(db_type, db_user, db_password, db_host, db_port, db_name, db_timeout)
    collection = BucketCollection(db, collection_name)
    return collection

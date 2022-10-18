from pymongo import MongoClient, errors
from src.database.entity import Database
from src.utils.log import get_logger


def get_mongo_connection_string(user: str, password: str, host: str, port: int) -> str:
    return f"mongodb://{user}:{password}@{host}:{port}"


class MongoDB(Database):
    def __init__(self, connection_string: str, database_name: str, db_timeout: int):
        super().__init__(connection_string)
        self.database_name = database_name
        self.db_timeout = db_timeout
        self.logger = get_logger(self.__class__.__name__)
        self.client = None
        self.db = None
        self.collection = None

    def connect(self):
        try:
            self.client = MongoClient(
                self.connection_string, serverSelectionTimeoutMS=self.db_timeout
            )
            self.logger.info("Connected to MongoDB server")
            self.db = self.client[self.database_name]
            self.logger.info(f"Connected to database: {self.database_name}")
        except errors.ServerSelectionTimeoutError as err:
            self.logger.error(f"Could not connect to MongoDB server: {err}")

    def create_collection(self, collection_name: str) -> None:
        try:
            collection = self.db[collection_name]
            self.logger.info(f"Created collection: {collection_name}")
            return collection
        except Exception as e:
            if "already exists" not in str(e):
                self.logger.error(f"Error creating collection: {e}")
            else:
                self.logger.info(
                    f"Collection already exists: {collection_name}, using existing collection"
                )

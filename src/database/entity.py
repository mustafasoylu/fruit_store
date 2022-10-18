from abc import ABC


class Database(ABC):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def connect(self):
        raise NotImplementedError()

    def create_collection(self):
        raise NotImplementedError()

    def delete_collection(self):
        raise NotImplementedError()


class Collection(ABC):
    def __init__(self, db: Database, collection_name: str):
        self.db = db
        self.collection = self.db.create_collection(collection_name)

    def insert(self):
        raise NotImplementedError()

    def set_index(self):
        raise NotImplementedError()

    def find(self):
        raise NotImplementedError()

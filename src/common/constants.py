from os import getenv

# main list for setting which fruits to be used in APIs
FRUITS = ["apple", "banana", "orange", "grape", "mango"]

# database related information
DB_TYPE = getenv("DB_TYPE", "MONGO")
DB_HOST = getenv("DB_HOST", "mongo")
DB_USER = getenv("DB_USER", "root")
DB_PASSWORD = getenv("DB_PASSWORD", "example")
DB_PORT = getenv("DB_PORT", "27017")
DB_NAME = getenv("DB_NAME", "test_db")
DB_COLLECTION_NAME = getenv("DB_COLLECTION_NAME", "bucket")
DB_TIMEOUT = int(getenv("DB_TIMEOUT", 1000))
BUCKET_LIMIT = int(getenv("BUCKET_LIMIT", 1000))
API_HOST = getenv("API_HOST", "0.0.0.0")
API_PORT = int(getenv("API_PORT", 80))
DEBUG = bool(getenv("DEBUG", False))

# MongoDB connection configuration.

import os

from pymongo import MongoClient

# Set MONGODB_URI in a local .env file or in the deployment environment.
client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))

# The database is created automatically when the first document is inserted.
db_client = client.test

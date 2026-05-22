from pymongo import MongoClient

from app.database.connection import Settings


client = MongoClient(Settings.MONGO_URI)

mongodb = client[Settings.MONGO_DATABASE]
from pymongo import MongoClient


from app.config.settings import settings

client = MongoClient(settings.MONGO_URI)

mongodb = client[settings.MONGO_DATABASE]
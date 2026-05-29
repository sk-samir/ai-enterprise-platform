from app.database.mongodb import mongodb


class MongoService:

    @staticmethod
    def insert_document(collection_name: str, document: dict):

        collection = mongodb[collection_name]

        result = collection.insert_one(document)

        return str(result.inserted_id)

    @staticmethod
    def get_documents(collection_name: str):

        collection = mongodb[collection_name]

        documents = list(collection.find({}, {"_id": 0}))

        return documents
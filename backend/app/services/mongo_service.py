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

        documents = list(
            collection.find({}, {"_id": 0})
        )

        return documents

    @staticmethod
    def count_documents(collection_name: str):

        collection = mongodb[collection_name]

        return collection.count_documents({})

    @staticmethod
    def get_documents_by_filter(
        collection_name: str,
        query: dict
    ):

        collection = mongodb[collection_name]

        documents = list(
            collection.find(query, {"_id": 0})
        )

        return documents
from app.services.mongo_service import MongoService


class MongoTool:

    @staticmethod
    def insert(collection: str, payload: dict):

        document_id = MongoService.insert_document(
            collection,
            payload
        )

        return {
            "status": "success",
            "inserted_id": document_id
        }

    @staticmethod
    def fetch(collection: str):

        documents = MongoService.get_documents(collection)

        return {
            "status": "success",
            "documents": documents
        }
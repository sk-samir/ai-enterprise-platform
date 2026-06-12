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
    
    @staticmethod
    def count(collection: str):

        total  = MongoService.count_documents(collection)

        return {
            "status": "success",
            "count": total 
        }
    
    @staticmethod
    def fetch_by_filter(collection: str, query: dict):

        documents = MongoService.get_documents_by_filter(collection, query)

        return {
            "status": "success",
            "documents": documents
        }
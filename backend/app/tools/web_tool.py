from app.services.web_search_service import WebSearchService


class WebTool:

    @staticmethod
    def search(query: str):

        results = WebSearchService.search(query)

        return {
            "tool": "web_search",
            "query": query,
            "results": results
        }
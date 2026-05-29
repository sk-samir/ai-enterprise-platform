from ddgs import DDGS
import logging


logger = logging.getLogger(__name__)


class WebSearchService:

    @staticmethod
    def search(query: str):

        results = []

        try:

            with DDGS() as ddgs:

                search_results = list(
                    ddgs.text(
                        query,
                        max_results=5
                    )
                )

                logger.info(search_results)

                for item in search_results:

                    results.append({
                        "title": item.get("title"),
                        "link": item.get("href"),
                        "snippet": item.get("body")
                    })

        except Exception as e:

            logger.error(f"Web search error: {str(e)}")

            return {
                "error": str(e)
            }

        return results
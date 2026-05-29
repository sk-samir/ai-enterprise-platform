class SQLValidator:

    @staticmethod
    def validate(query: str):

        lower_query = query.lower().strip()

        if not lower_query.startswith("select"):
            return False

        blocked_keywords = [
            "delete",
            "drop",
            "update",
            "insert",
            "alter",
            "truncate"
        ]

        return not any(
            keyword in lower_query
            for keyword in blocked_keywords
        )
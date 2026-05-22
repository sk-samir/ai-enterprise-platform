class SQLValidator:

    ALLOWED_KEYWORDS = [
        "select"
    ]

    @staticmethod
    def validate(query: str):

        lower_query = query.lower()

        return any(
            keyword in lower_query
            for keyword in SQLValidator.ALLOWED_KEYWORDS
        )
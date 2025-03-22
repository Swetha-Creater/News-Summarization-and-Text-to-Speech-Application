from utils import gemini_query_handler

class NewsQueryAgent:
    def __init__(self, news_data: dict):
        self.news_data = news_data

    def ask(self, user_query: str) -> str:
        return gemini_query_handler(user_query, self.news_data)

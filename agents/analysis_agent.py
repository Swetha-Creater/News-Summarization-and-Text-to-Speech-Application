from utils import analyze_news_trends

class NewsAnalysisAgent:
    def __init__(self, company_name: str):
        self.company_name = company_name

    def run(self):
        return analyze_news_trends(self.company_name)

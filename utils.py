import os
import json
import requests
import nltk
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai
from yake import KeywordExtractor
from collections import Counter

# Ensure NLTK data is downloaded
nltk.download("vader_lexicon")

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API Key missing! Please set GEMINI_API_KEY in .env")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


def fetch_latest_news(query: str) -> list:
    """Fetches top 10 news articles from Google News RSS."""
    try:
        search_url = f"https://news.google.com/rss/search?q={query}"
        response = requests.get(search_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "xml")

        articles = soup.find_all("item")[:10]
        return [
            {
                "Title": article.title.text,
                "Link": article.guid.text if article.guid else article.link.text,
                "Source": article.source.text if article.source else "Unknown",
                "Published Date": article.pubDate.text
            }
            for article in articles
        ]
    except Exception as error:
        print(f" Error fetching news: {error}")
        return []


def generate_summary(text: str) -> str:
    """Generates a summary using Gemini."""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"Summarize the following article in 3 sentences:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as error:
        print(f" Error generating summary: {error}")
        return "Summary unavailable"


def assess_sentiment(text: str) -> str:
    """Determines sentiment polarity."""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = (
            "Analyze this text's sentiment and return only "
            "'Positive', 'Negative', or 'Neutral':\n\n" + text
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as error:
        print(f"Sentiment analysis failed: {error}")
        return "Neutral"


def extract_key_topics(text: str, count: int = 3) -> list:
    """Extracts important keywords/topics using YAKE."""
    topic_extractor = KeywordExtractor(n=2, top=count)
    key_terms = topic_extractor.extract_keywords(text)
    return [term[0] for term in key_terms]


def comparative_analysis(news_data: list) -> dict:
    """Performs sentiment and topic trend analysis across articles."""
    if len(news_data) < 2:
        return {"Error": "Not enough articles available for meaningful comparison."}

    sentiment_distribution = Counter(article["Sentiment"] for article in news_data)

    prompt_text = (
        "Provide bullet-pointed comparisons for sentiment and topic shifts "
        "across the following news articles:\n\n"
    )

    for i in range(len(news_data) - 1):
        prompt_text += (
            f"Article {i + 1}: {news_data[i]['Title']} "
            f"(Sentiment: {news_data[i]['Sentiment']}) ➝ "
            f"Article {i + 2}: {news_data[i + 1]['Title']} "
            f"(Sentiment: {news_data[i + 1]['Sentiment']})\n"
            f"Topics Shift: {news_data[i]['Topics']} ➝ {news_data[i + 1]['Topics']}\n\n"
        )

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt_text)
        coverage_differences = response.text.strip()
    except Exception as error:
        print(f"Gemini AI Error: {error}")
        coverage_differences = "- AI Analysis Unavailable\n- Unable to retrieve insights"

    all_topics = [set(article["Topics"]) for article in news_data]
    common_topics = set.intersection(*all_topics) if all_topics else set()

    unique_topics_per_article = [
        f"- **Article {i + 1} Unique Topics:** {', '.join(all_topics[i] - common_topics) or 'None'}"
        for i in range(len(all_topics))
    ]

    try:
        prompt_summary = (
            "Summarize the overall sentiment trend across articles "
            "in a **concise** business insight:\n\n"
            f"Sentiment Distribution: {sentiment_distribution}\n"
            f"Coverage Differences:\n{coverage_differences}\n"
            f"Common Topics: {list(common_topics)}"
        )
        response_summary = model.generate_content(prompt_summary)
        final_analysis = response_summary.text.strip()
    except Exception as error:
        print(f"Gemini AI Summary Error: {error}")
        final_analysis = "AI Summary Unavailable"

    return {
        "Sentiment Distribution": sentiment_distribution,
        "Coverage Differences (Markdown)": coverage_differences,
        "Topic Overlap (Markdown)": f"""
**Common Topics:** {', '.join(common_topics) or 'None'}

**Unique Topics per Article:**
{chr(10).join(unique_topics_per_article)}
""",
        "Final Insight": final_analysis
    }


def analyze_news_trends(company_name: str) -> dict:
    """Fetches, processes, and analyzes news for a company."""
    try:
        articles = fetch_latest_news(company_name)
        if not articles:
            return {"error": "No relevant news articles found."}

        processed_report = {"Company": company_name, "Articles": []}

        for article in articles:
            summary = generate_summary(article["Title"])
            sentiment = assess_sentiment(summary)
            topics = extract_key_topics(summary)

            processed_report["Articles"].append({
                "Title": article["Title"],
                "Link": article["Link"],
                "Summary": summary,
                "Sentiment": sentiment,
                "Topics": topics
            })

        processed_report["Sentiment Comparison"] = comparative_analysis(
            processed_report["Articles"]
        )

        return processed_report

    except Exception as error:
        return {"error": str(error)}


def gemini_query_handler(user_query: str, article_data: dict) -> str:
    """Gemini-powered query handler for processed news data."""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = (
            "You are an intelligent assistant analyzing news articles about a company. "
            "Here's the data in JSON format:\n\n"
            f"{json.dumps(article_data, indent=2)}\n\n"
            f"Now, answer this user question in 3-5 sentences:\n\"{user_query}\""
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"











---
title: NewsSummary Query
emoji: 🐢
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.43.2
app_file: app.py
pinned: false
license: mit
---

# **AI-Agents NewsWise**

AI-Agents NewsWise is a multi-agent, AI-powered news analysis system that fetches, summarizes, and interprets the latest news articles for any company or topic of interest. It leverages Google Gemini models for summarization and querying, sentiment classification, and key topic extraction all packaged in an interactive Streamlit UI backed by a FastAPI server.

## Features:

- **News Extraction**: Fetches and parses the latest news articles about a company using web scraping from google news.
- **Text Summarization**: Uses Gemini API to generate concise summaries for each news article.
- **Sentiment Analysis**: Detects and classifies the sentiment (Positive, Negative, Neutral) of each article.
- **Topic Detection**: Extracts key topics and entities using YAKE and NLP techniques for topic clustering.
- **Comparative Analysis**: Compares sentiment distribution, topic overlap, and coverage differences across articles.
- **Query-based Insights**: Supports follow-up questions from users using a custom Query Agent powered by Gemini to extract intelligent insights.
- **Text-to-Speech**: Converts the final summarized insight into Hindi audio using gTTS.
- **Streamlit UI**: Interactive and user-friendly dashboard to enter company names, view analysis, ask questions, and listen to the Hindi audio summary.
- **FastAPI Backend**: Robust API that performs heavy processing and serves the data to the frontend.
- **Agent-Based Modular Architecture**: Clean separation of concerns using analysis_agent and query_agent for scalability and maintenance.


## Installation Steps:

1. Clone the Repository:

   ```bash
   git clone https://github.com/Swetha-Creater/News-Summarization-and-Text-to-Speech-Application.git
   cd News-Summarization-and-Text-to-Speech-Application
   
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   
5. Install Dependencies:
    ```bash
   pip install -r requirements.txt
   
7. Add API Keys in `.env`:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key
   
9. Run the Application:
    ```bash
   streamlit run app.py

## Project Structure

![image](https://github.com/user-attachments/assets/a1310c26-0e1f-48b8-91ad-9b9bfdb0c4c4)

   
## Model Details

### Summarization
• Model: gemini-2.0-flash by Google.

• Purpose: To summarize news articles into 2-3 lines.

• Implementation: Prompt-based summarization using Google Generative AI API.

### Sentiment Analysis

• Model: gemini-2.0-flash

• Purpose: Determine article sentiment – Positive, Negative, or Neutral.

• Implementation: Prompt-based zero-shot sentiment classification.

### Text-to-Speech (TTS)
• Model: gTTS (Google Text-to-Speech).

• Purpose: Convert final business insight into Hindi audio.

• Implementation: Generates .mp3 from the final insight using gTTS.

### API Development

The application exposes API endpoints for communication between the frontend and backend:

GET /analyze/?company={company_name}: Fetches news articles for a given company and perform analysis and query system.

### Third-Party API Usage
• Google Gemini: Summarization, Sentiment, Query (google-generativeai SDK)

• gTTS (Google TTS): Hindi audio output (gtts library)

• Google News RSS: News articles fetching (requests + BeautifulSoup)

 ### Comparative Analysis
 Comparative Analysis examines differences and similarities in news coverage across articles. It highlights variations in sentiment, topic overlap, and 
 coverage intensity for better contextual understanding.

## Assumptions

• The company name returns relevant articles from Google News.

• The user has a valid Gemini API key.

• The system is expected to run locally or on Hugging Face.

## Future Improvements

1. **Multilingual Support**:Add support for more languages (Tamil, Telugu, Kannada, etc.) for both summary and TTS using gTTS, Bark, or Google Translate API.

2. **Live News Stream**: Integrate with live news APIs (e.g., NewsAPI, GNews) to fetch real-time news.

3. **Voice-based Input & Output**: Allow users to speak their queries using speech recognition.
---
## Demo
## 🎥 Demo

<video src="demo.webm" controls style="width: 100%; max-width: 700px; border-radius: 10px;">
</video>





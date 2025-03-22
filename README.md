# **AI-Agents NewsWise**

AI-Agents NewsWise is a multi-agent, AI-powered news analysis system that fetches, summarizes, and interprets the latest news articles for any company or topic of interest. It leverages Google Gemini models for summarization and querying, sentiment classification, and key topic extraction — all packaged in an interactive Streamlit UI backed by a FastAPI server.

### Features:
- News Extraction: Fetches and parses the latest news articles about a company using web scraping from google news.
- Text Summarization: Uses Gemini API to generate concise summaries for each news article.
- Sentiment Analysis: Detects and classifies the sentiment (Positive, Negative, Neutral) of each article.
- Topic Detection: Extracts key topics and entities using YAKE and NLP techniques for topic clustering.
- Comparative Analysis: Compares sentiment distribution, topic overlap, and coverage differences across articles.
- Query-based Insights: Supports follow-up questions from users using a custom Query Agent powered by Gemini to extract intelligent insights.
- Text-to-Speech: Converts the final summarized insight into Hindi audio using gTTS.
- Streamlit UI: Interactive and user-friendly dashboard to enter company names, view analysis, ask questions, and listen to the Hindi audio summary.
- FastAPI Backend: Robust API that performs heavy processing and serves the data to the frontend.
- Agent-Based Modular Architecture: Clean separation of concerns using analysis_agent and query_agent for scalability and maintenance.

### 1. Project Setup
•	Requirements:
• Python 3.9+
• pip
• Internet access (for APIs)

###•	Installation Steps:

1. Clone the Repository:

   ```bash
   git clone https://github.com/Swetha-Creater/News-Summarization-and-Text-to-Speech-Application.git
   cd ai-agents-newswise
   
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
   
## Model Details

### Summarization
• Model: gemini-2.0-flash by Google
• Purpose: To summarize news articles into 2-3 lines.
• Implementation: Prompt-based summarization using Google Generative AI API.

### Sentiment Analysis
• Model: gemini-2.0-flash
• Purpose: Determine article sentiment – Positive, Negative, or Neutral.
• Implementation: Prompt-based zero-shot sentiment classification.

### Text-to-Speech (TTS)
• Model: gTTS (Google Text-to-Speech)
• Purpose: Convert final business insight into Hindi audio.
• Implementation: Generates .mp3 from the final insight using gTTS.

### API Development

Backend service uses FastAPI running on localhost:8000
Exposed Endpoint:
GET /analyze/?company=<company_name>
Returns summarized articles, sentiment analysis, keyword extraction, and final insight with Hindi audio.
Testing via Postman:
Endpoint: http://localhost:8000/analyze/?company=TCS
Method: GET
Headers: None required
Response: JSON with insights

### Third-Party API Usage
• Google Gemini: Summarization, Sentiment, Query (google-generativeai SDK)

• gTTS (Google TTS): Hindi audio output (gtts library)

• Google News RSS: News articles fetching (requests + BeautifulSoup)

 ### Comparative Analysis
 Comparative Analysis examines differences and similarities in news coverage across articles. It highlights variations in sentiment, topic overlap, and 
 coverage intensity for better contextual understanding.

## Assumptions & Limitations
Assumptions
• The company name returns relevant articles from Google News.
• The user has a valid Gemini API key.
• The system is expected to run locally or on Hugging Face.

### Future Improvements

1. Multilingual Support
Add support for more languages (Tamil, Telugu, Kannada, etc.) for both summary and TTS using gTTS, Bark, or Google Translate API.

2. Live News Stream
Integrate with live news APIs (e.g., NewsAPI, GNews) to fetch real-time news.

3. Voice-based Input & Output
Allow users to speak their queries using speech recognition.



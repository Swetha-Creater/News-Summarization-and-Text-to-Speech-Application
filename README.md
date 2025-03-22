# **AI-Agents NewsWise**

## Project Overview

AI-Agents NewsWise is a multi-agent, AI-powered news analysis system that fetches, summarizes, and interprets the latest news articles for any company or topic of interest. It leverages Google Gemini models for summarization and querying, sentiment classification, and key topic extraction — all packaged in an interactive Streamlit UI backed by a FastAPI server.

### 1. Project Setup
•	Requirements:
• Python 3.9+
• pip
• Internet access (for APIs)

###•	Installation Steps:

1. Clone the Repository:
   git clone https://github.com/your-username/ai-agents-newswise.git
   cd ai-agents-newswise
2. Create a virtual environment (optional but recommended):
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
3. Install Dependencies:
   pip install -r requirements.txt
4. Add API Keys in `.env`:
   GEMINI_API_KEY=your_gemini_api_key
5. Run the Application:
   streamlit run app.py
2. Model Details

Summarization
• Model: gemini-2.0-flash by Google
• Purpose: To summarize news articles into 2-3 lines.
• Implementation: Prompt-based summarization using Google Generative AI API.

Sentiment Analysis
• Model: gemini-2.0-flash
• Purpose: Determine article sentiment – Positive, Negative, or Neutral.
• Implementation: Prompt-based zero-shot sentiment classification.

Text-to-Speech (TTS)
• Model: gTTS (Google Text-to-Speech)
• Purpose: Convert final business insight into Hindi audio.
• Implementation: Generates .mp3 from the final insight using gTTS.

4. API Development
Backend service uses FastAPI running on localhost:8000
Exposed Endpoint:
GET /analyze/?company=<company_name>
Returns summarized articles, sentiment analysis, keyword extraction, and final insight with Hindi audio.
Testing via Postman:
Endpoint: http://localhost:8000/analyze/?company=TCS
Method: GET
Headers: None required
Response: JSON with insights

5. Third-Party API Usage
• Google Gemini: Summarization, Sentiment, Query (google-generativeai SDK)
• gTTS (Google TTS): Hindi audio output (gtts library)
• Google News RSS: News articles fetching (requests + BeautifulSoup)

6. Assumptions & Limitations
Assumptions
• The company name returns relevant articles from Google News.
• The user has a valid Gemini API key.
• The system is expected to run locally or on Hugging Face.
Limitations
• Gemini API may return incomplete or rate-limited responses.
• RSS feeds might lack enough articles.
• gTTS may fail on long/malformed inputs.  
• Summarization quality relies on Gemini's context interpretation.



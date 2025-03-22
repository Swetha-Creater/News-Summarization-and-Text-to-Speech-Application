import streamlit as st
import subprocess
import threading
import time
import requests
from agents.analysis_agent import NewsAnalysisAgent
from agents.query_agent import NewsQueryAgent
from audio import HindiInsightSpeaker


def start_fastapi():
    subprocess.Popen([
        "uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"
    ])


def main():
    # Start FastAPI only once
    if "fastapi_started" not in st.session_state:
        threading.Thread(target=start_fastapi, daemon=True).start()
        st.session_state["fastapi_started"] = True
        time.sleep(2)  # Wait for FastAPI to fully start

    # Streamlit UI setup
    st.set_page_config(
        page_title="AI-Powered News Analyser and Query System", layout="wide"
    )
    st.title("AI-Agents NewsWise")
    st.write("Enter a company name below to analyze its latest news coverage and trends.")

    company_name = st.text_input("Enter Company Name:", "")

    # Run analysis
    if st.button("Analyze News"):
        if company_name:
            with st.spinner(" Calling backend to analyze..."):
                try:
                    response = requests.get(
                        f"http://localhost:8000/analyze/?company={company_name}"
                    )
                    news_report = response.json()

                    if "error" in news_report:
                        st.error(news_report["error"])
                    else:
                        st.session_state["news_report"] = news_report
                        st.session_state["company_name"] = company_name
                        st.success("Analysis Completed!")
                except Exception as e:
                    st.error(f"🚨 Backend Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter a company name first.")

    #  Always display previous analysis if available
    if "news_report" in st.session_state and "company_name" in st.session_state:
        news_report = st.session_state["news_report"]
        company_name = st.session_state["company_name"]

        st.subheader(f"📰 News Analysis for {company_name}")
        for idx, article in enumerate(news_report["Articles"], start=1):
            st.markdown(f"### {idx}. {article['Title']}")
            st.markdown(f"- **Summary**: {article['Summary']}")
            st.markdown(f"- **Sentiment**: {article['Sentiment']}")
            st.markdown(f"- **Topics**: {', '.join(article['Topics'])}")
            st.markdown("---")

        comparison_data = news_report["Sentiment Comparison"]
        st.subheader(" Comparative Sentiment Analysis")

        st.markdown("#### Sentiment Distribution")
        for sentiment in ["Positive", "Negative", "Neutral"]:
            count = comparison_data.get("Sentiment Distribution", {}).get(sentiment, 0)
            st.markdown(f"- {sentiment}: {count}")

        st.markdown("#### Coverage Differences")
        st.markdown(comparison_data["Coverage Differences (Markdown)"])

        st.markdown("#### Topic Overlap")
        st.markdown(comparison_data["Topic Overlap (Markdown)"])

        st.markdown("#### Final Insight")
        st.info(comparison_data["Final Insight"])

        # Hindi audio
        if "HindiAudio" in news_report:
            audio_result = news_report["HindiAudio"]
            if audio_result["success"]:
                st.audio(audio_result["audio_file"])
                st.markdown(f"**Hindi Translation:** {audio_result['hindi_text']}")
            else:
                st.error(audio_result["message"])

        # Key topics
        st.subheader("Key Topics in News")
        all_topics = [
            topic
            for article in news_report["Articles"]
            for topic in article.get("Topics", [])
        ]
        if all_topics:
            st.write(" | ".join(set(all_topics)))
        else:
            st.warning("No topics extracted.")

    # Follow-up Query Section
    if "news_report" in st.session_state:
        st.subheader("Ask a Question About the News")
        user_query = st.text_input("Enter your query (e.g., 'What is the most discussed topic?')")

        if user_query:
            with st.spinner("Gemini is analyzing your question..."):
                query_agent = NewsQueryAgent(st.session_state["news_report"])
                answer = query_agent.ask(user_query)

            st.markdown("### Gemini's Answer")
            st.success(answer)


# Entry point
if __name__ == "__main__":
    main()




















from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils import analyze_news_trends
from audio import HindiInsightSpeaker
import uvicorn

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain(s) in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/analyze/")
def analyze(company: str):
    result = analyze_news_trends(company)

    if "error" in result:
        return {"error": result["error"]}

    speaker = HindiInsightSpeaker()
    audio_response = speaker.generate_hindi_speech(
        result["Sentiment Comparison"]["Final Insight"]
    )

    result["HindiAudio"] = audio_response.get("audio_base64")
    result["HindiText"] = audio_response.get("hindi_text")
    result["Message"] = audio_response.get("message")

    return result


# Optional: Run directly using `python backend.py`
def main():
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()



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
    """
    Main API endpoint to analyze company news.
    Returns structured report including sentiment, topics, and Hindi audio.
    """
    result = analyze_news_trends(company)

    if "error" in result:
        return {"error": result["error"]}

    speaker = HindiInsightSpeaker()
    audio_data = speaker.generate_hindi_speech(
        result["Sentiment Comparison"]["Final Insight"]
    )

    result["HindiAudio"] = audio_data
    return result


# Optional: Run directly using `python backend.py`
def main():
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
        try:
            cleaned_text = self.clean_text(final_insight)
            hindi_text = self.translate_to_hindi(cleaned_text)
            audio_path = os.path.join(self.temp_dir, f"hindi_insight_{hash(hindi_text) % 10000}.mp3")

            tts = gTTS(text=hindi_text, lang='hi', slow=False)
            tts.save(audio_path)

            return {
                "success": True,
                "hindi_text": hindi_text,
                "audio_file": audio_path,
                "message": " Hindi audio generated successfully."
            }
        except Exception as e:
            return {
                "success": False,
                "hindi_text": None,
                "audio_file": None,
                "message": f" Error generating audio: {str(e)}"
            }



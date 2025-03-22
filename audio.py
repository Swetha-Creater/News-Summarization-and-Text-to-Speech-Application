import os
import tempfile
import re
from typing import Dict, Any
from gtts import gTTS
from deep_translator import GoogleTranslator


class HindiInsightSpeaker:
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()

    def clean_text(self, text: str) -> str:
        """Clean the text for translation and TTS."""
        text = re.sub(r"http\S+", "", text)
        text = re.sub(r"[^\w\s.,?!;:\-\'\"()]", " ", text)
        return re.sub(r"\s+", " ", text).strip()

    def translate_to_hindi(self, text: str) -> str:
        """Translate English text to Hindi using Deep Translator."""
        try:
            return GoogleTranslator(source='auto', target='hi').translate(text)
        except Exception as e:
            print(" Translation Error:", e)
            return "अनुवाद में त्रुटि हुई। कृपया पुनः प्रयास करें।"

    def generate_hindi_speech(self, final_insight: str) -> Dict[str, Any]:
        """Convert final insight to Hindi speech using gTTS."""
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



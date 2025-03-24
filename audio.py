import os
import tempfile
import re
from typing import Dict, Any
from gtts import gTTS
from deep_translator import GoogleTranslator
import base64
from io import BytesIO
import time 


class HindiInsightSpeaker:
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
            print("Translation Error:", e)
            return "अनुवाद में त्रुटि हुई। कृपया पुनः प्रयास करें।"

    def generate_hindi_speech(self, final_insight: str) -> Dict[str, Any]:
        """Convert final insight to Hindi speech using gTTS, return base64 directly."""
        try:
            cleaned_text = self.clean_text(final_insight)
            hindi_text = self.translate_to_hindi(cleaned_text)

            # Add a delay to avoid 429 Too Many Requests
            time.sleep(2)

            # Generate audio in memory (no saving to file)
            tts = gTTS(text=hindi_text, lang='hi', slow=False)
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)

            audio_base64 = base64.b64encode(audio_buffer.read()).decode("utf-8")

            return {
                "success": True,
                "hindi_text": hindi_text,
                "audio_base64": audio_base64,
                "message": "Hindi audio generated successfully."
            }

        except Exception as e:
            return {
                "success": False,
                "hindi_text": None,
                "audio_base64": None,
                "message": f"Error generating audio: {str(e)}"
            }



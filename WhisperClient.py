import openai
import base64

from typing import Union
from BaseClient import BaseClient

class WhisperClient(BaseClient):
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def respond(self, messages):
        audio_bytes = messages.download()
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        transcription = self.transcribe(base64_encoded_file=audio_base64, language='en-US')
        
        return transcription
import openai

from BaseClient import BaseClient

class WhisperClient(BaseClient):
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def respond(self, messages):    
        pass   
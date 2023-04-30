import openai

import const

from BaseClient import BaseClient

class DalleClient(BaseClient):
    def __init__(self, api_key):
        openai.api_key = api_key

    def respond(self, messages):
        response = openai.Image.create(
            prompt = messages,
            n = 1,
            size = "256x256"
        )
        return response["data"][0]["url"]
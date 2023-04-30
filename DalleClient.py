import openai

import const

from BaseClient import BaseClient

class DalleClient(BaseClient):
    def __init__(self):
        openai.api_key = const.OPENAI_API_KEY
        self.user = input()
    
    def image_generate(self):
        response = openai.Image.create(
            prompt = self.user,
            n = 1,
            size = "256x256"
        )

        return response["data"][0]["url"]
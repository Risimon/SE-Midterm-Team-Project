import openai

import const

from BaseClient import BaseClient

class DalleClient(BaseClient):
    """Class for working with Dalle API. Inherits from BaseClient"""
    def __init__(self, api_key):
        #set the API KEY
        openai.api_key = api_key
    
    # generate the image and return the URL
    def respond(self, messages):
        response = openai.Image.create(
            prompt = messages,
            n = 1,
            size = "256x256"
        )
        return response["data"][0]["url"]

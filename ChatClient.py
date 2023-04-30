import openai
from const import CHAT_PROMPT

from BaseClient import BaseClient


class ChatClient(BaseClient):
    """ ChatClient class for working with GPT3.5 API. Inherits from BaseClient"""
    def __init__(self, api_key):
        # API model. Other options can be obtained via OpenAI official website
        self.model = "gpt-3.5-turbo"
        openai.api_key = api_key
    
    # make a call to the API and return the answer
    def respond(self, message_list):
        # add prompt for context in chatGPT
        prompt = CHAT_PROMPT % message_list[0]["content"]
        messages = [{"role": "system", "content": prompt}]
        messages.extend(message_list[1:])
        # call to the API
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )
        # return the whole conversation 
        messages.append(completion.choices[0].message)
        return messages

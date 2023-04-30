import openai
from const import CHAT_PROMPT

from BaseClient import BaseClient


class ChatClient(BaseClient):
    def __init__(self, api_key):
        self.model = "gpt-3.5-turbo"
        openai.api_key = api_key

    def respond(self, message_list):
        prompt = CHAT_PROMPT % message_list[0]["content"]
        messages = [{"role": "system", "content": prompt}]
        messages.extend(message_list[1:])
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )
        messages.append(completion.choices[0].message)
        return messages

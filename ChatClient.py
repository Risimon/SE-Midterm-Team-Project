import os
import openai
from const import CHAT_PROMPT

from BaseClient import BaseClient


class ChatClient(BaseClient):
    def __init__(self, mode):
        self.model = "gpt-3.5-turbo"
        self.mode = mode

    def respond(self, message_list):
        prompt = CHAT_PROMPT % message_list[0]
        messages = [{"role": "system", "content": prompt}, message_list[1:]]
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=messages
        )
        messages.append(completion.choices[0].message)
        return messages

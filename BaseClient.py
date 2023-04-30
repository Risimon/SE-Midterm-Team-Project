from abc import ABC, abstractmethod
import const
import openai
import os


class BaseClient(ABC):
    openai.api_key = os.getenv(const.OPENAI_API_KEY)

    @abstractmethod
    def respond(self, messages):
        pass

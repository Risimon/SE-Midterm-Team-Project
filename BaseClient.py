from abc import ABC, abstractmethod
from dotenv import load_dotenv
import const
import openai
import os


class BaseClient(ABC):
    """Base client class that other client classes (e.g voice recognition) will inherit from"""
    openai.api_key = os.getenv(const.OPENAI_API_KEY)

    @abstractmethod
    def respond(self, messages):
        pass


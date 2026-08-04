from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


class LLM:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY")
        )

    def get_llm(self):

        return self.llm
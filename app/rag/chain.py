from app.rag.retriever import Retriever
from app.llm.llm import LLM
from app.llm.prompt import SYSTEM_PROMPT


class RAGChain:

    def __init__(self, username):

        self.retriever = Retriever(
            persist_directory=f"storage/users/{username}/chroma_db"
        )

        self.llm = LLM().get_llm()

    def ask(self, question):

        docs = self.retriever.retrieve(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.llm.invoke(prompt)

        return response.content



from langchain_community.vectorstores import Chroma

from app.rag.embeddings import EmbeddingModel


class Retriever:

    def __init__(self, persist_directory):

        embedding = EmbeddingModel.get_embedding()

        self.vector_db = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding
        )

    def retrieve(self, question):

        retriever = self.vector_db.as_retriever(
            search_kwargs={"k": 3}
        )

        return retriever.invoke(question) 
"""
# old version

class Retriever:

    def __init__(self, persist_directory):

        embedding = EmbeddingModel().get_embedding()

        self.vector_db = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding
        )

    def retrieve(self, question):

        retriever = self.vector_db.as_retriever(
            search_kwargs={"k": 3}
        )

        return retriever.invoke(question)
"""

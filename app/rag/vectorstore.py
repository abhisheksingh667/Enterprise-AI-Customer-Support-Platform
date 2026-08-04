from langchain_community.vectorstores import Chroma


class VectorStore:

    def __init__(self, embedding, persist_directory):

        self.embedding = embedding
        self.persist_directory = persist_directory

    def create(self, chunks):

        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding,
            persist_directory=self.persist_directory
        )

        return vectordb
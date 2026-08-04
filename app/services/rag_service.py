from app.rag.chain import RAGChain


class RAGService:

    def __init__(self, username):

        self.chain = RAGChain(username)

    def search(self, question):

        return self.chain.ask(question)
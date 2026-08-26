from langchain_huggingface import HuggingFaceEmbeddings


_embedding_model = None


class EmbeddingModel:

    @staticmethod
    def get_embedding():

        global _embedding_model

        if _embedding_model is None:
            print("Loading embedding model...")

            _embedding_model = HuggingFaceEmbeddings(
                model_name="BAAI/bge-small-en-v1.5"
            )

        return _embedding_model
"""
# old version
@lru_cache(maxsize=1)
class EmbeddingModel:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def get_embedding(self):

        return self.embedding
"""

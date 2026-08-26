from functools import lru_cache
from langchain_huggingface import HuggingFaceEmbeddings


@lru_cache(maxsize=1)
def get_embedding_model():

    print("Loading embedding model...")

    return HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )


class EmbeddingModel:

    def get_embedding(self):
        return get_embedding_model()
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

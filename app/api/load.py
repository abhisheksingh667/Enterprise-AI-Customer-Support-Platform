from fastapi import APIRouter, Depends
from pathlib import Path

from app.auth.dependencies import get_current_user

from app.rag.loader import PDFLoader
from app.rag.splitter import DocumentSplitter
from app.rag.embeddings import EmbeddingModel
from app.rag.vectorstore import VectorStore

router = APIRouter(
    prefix="/api/v1/load",
    tags=["Loader"]
)


@router.post("/")
def load_documents(
    current_user=Depends(get_current_user)
):

    # Current user's PDF folder
    pdf_folder = Path(
        f"storage/users/{current_user.username}/uploaded_pdfs"
    )

    loader = PDFLoader()
    splitter = DocumentSplitter()

    embedding_model = EmbeddingModel()
    embedding = embedding_model.get_embedding()

    # Current user's ChromaDB folder
    vectorstore = VectorStore(
        embedding=embedding,
        persist_directory=f"storage/users/{current_user.username}/chroma_db"
    )

    all_documents = []

    for pdf in pdf_folder.glob("*.pdf"):

        # Load PDF
        docs = loader.load(str(pdf))

        # Split into chunks
        chunks = splitter.split(docs)

        # Store chunks
        all_documents.extend(chunks)

    # Create Chroma Vector Database
    vectorstore.create(all_documents)

    return {
        "status": "Success",
        "user": current_user.username,
        "total_chunks": len(all_documents),
        "vector_database": "Created Successfully"
    }
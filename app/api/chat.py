from functools import lru_cache

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.services.rag_service import RAGService
from app.auth.dependencies import get_current_user

from app.database.session import get_db
from app.database.crud import save_chat

router = APIRouter(
    prefix="/api/v1/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):
    question: str


@lru_cache(maxsize=1)
def get_rag_service_class():
    """
    Lazily import the RAG service.
    This prevents AI-related dependencies from loading
    immediately during application startup.
    """
    from app.services.rag_service import RAGService
    return RAGService

@router.post("/")
def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

     # Lazy-load RAGService only when chat endpoint is called
    RAGService = get_rag_service_class()
    
    # Generate Answer
    rag_service = RAGService(current_user.username)
    answer = rag_service.search(request.question)

    # Save Chat History
    save_chat(
        db=db,
        user_id=current_user.id,
        question=request.question,
        answer=answer
    )

    return {
        "user": current_user.username,
        "question": request.question,
        "answer": answer
    }
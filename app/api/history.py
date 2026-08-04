from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.database.crud import get_chat_history, delete_chat_history

router = APIRouter(
    prefix="/api/v1/history",
    tags=["History"]
)


@router.get("/")
def history(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    chats = get_chat_history(
        db,
        current_user.id
    )

    return chats


@router.delete("/")
def clear_history(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    delete_chat_history(
        db,
        current_user.id
    )

    return {
        "message": "Chat history deleted successfully."
    }
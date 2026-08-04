from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.database.crud import (
    get_chat_by_id,
    update_feedback
)

from app.schemas.feedback import FeedbackRequest

router = APIRouter(
    prefix="/api/v1/feedback",
    tags=["Feedback"]
)


@router.post("/")
def feedback(
    request: FeedbackRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    chat = get_chat_by_id(
        db,
        request.chat_id
    )

    if chat is None:
        return {
            "message": "Chat not found"
        }

    if chat.user_id != current_user.id:
        return {
            "message": "Unauthorized"
        }

    update_feedback(
        db,
        request.chat_id,
        request.feedback
    )

    return {
        "message": "Feedback Saved Successfully"
    }
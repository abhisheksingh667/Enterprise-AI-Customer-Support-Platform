from fastapi import APIRouter

from app.schemas.message import Message

router = APIRouter(
    prefix="/message",
    tags=["Message"]
)


@router.post("/")
def receive_message(data: Message):

    return {
        "name": data.name,
        "question": data.question,
        "status": "Received Successfully"
    }
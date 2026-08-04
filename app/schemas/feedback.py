from pydantic import BaseModel


class FeedbackRequest(BaseModel):
    chat_id: int
    feedback: str
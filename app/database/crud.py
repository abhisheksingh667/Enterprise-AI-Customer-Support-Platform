from sqlalchemy.orm import Session

from app.database.models import User, ChatHistory


# ---------------- USER ---------------- #

def get_user_by_username(db: Session, username: str):

    return db.query(User).filter(
        User.username == username
    ).first()


def create_user(db: Session, username: str, hashed_password: str):

    user = User(
        username=username,
        hashed_password=hashed_password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user(db: Session, username: str):

    return db.query(User).filter(
        User.username == username
    ).first()


# ---------------- CHAT HISTORY ---------------- #

def save_chat(
    db: Session,
    user_id: int,
    question: str,
    answer: str
):

    chat = ChatHistory(
        user_id=user_id,
        question=question,
        answer=answer
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


def get_chat_history(
    db: Session,
    user_id: int
):

    return (
        db.query(ChatHistory)
        .filter(ChatHistory.user_id == user_id)
        .order_by(ChatHistory.created_at.desc())
        .all()
    )


def delete_chat_history(
    db: Session,
    user_id: int
):

    db.query(ChatHistory).filter(
        ChatHistory.user_id == user_id
    ).delete()

    db.commit()

    # ---------------- FEEDBACK ---------------- #

def update_feedback(
    db: Session,
    chat_id: int,
    feedback: str
):

    chat = db.query(ChatHistory).filter(
        ChatHistory.id == chat_id
    ).first()

    if chat is None:
        return None

    chat.feedback = feedback

    db.commit()
    db.refresh(chat)

    return chat


def get_chat_by_id(
    db: Session,
    chat_id: int
):

    return db.query(ChatHistory).filter(
        ChatHistory.id == chat_id
    ).first()
from fastapi import FastAPI

from app.api.home import router as home_router
from app.api.health import router as health_router
from app.api.message import router as message_router
from app.api.upload import router as upload_router
from app.api.load import router as load_router
from app.api.chat import router as chat_router
from app.api.auth import router as auth_router
from app.api.history import router as history_router
from app.api.feedback import router as feedback_router

from app.database.database import engine
from app.database.models import Base
from app.exceptions.handlers import register_exception_handlers

# Create all tables
Base.metadata.create_all(bind=engine)

print("Tables Created Successfully")

app = FastAPI(
    title="Enterprise AI Customer Support Platform",
    version="1.0.0"
)

register_exception_handlers(app)
app.include_router(home_router)
app.include_router(health_router)
app.include_router(message_router)
app.include_router(upload_router)
app.include_router(load_router)
app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(history_router)
app.include_router(feedback_router)
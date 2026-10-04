from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc)

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    user_message = Column(String)
    bot_response = Column(String)
    intent = Column(String)
    confidence = Column(Float)
    language = Column(String)
    timestamp = Column(DateTime, default=utc_now)

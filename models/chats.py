from sqlalchemy import Column, BIGINT, VARCHAR, JSON
from database.connection import Base

class Chat(Base):
    __tablename__ = "chats"

    version = Column(VARCHAR(255), nullable=False)
    chat_id = Column(VARCHAR(36), nullable=False, primary_key=True)
    time = Column(BIGINT, nullable=False)
    message = Column(VARCHAR(255), nullable=False)
    room = Column(JSON, nullable=False)
    user = Column(JSON, nullable=False)
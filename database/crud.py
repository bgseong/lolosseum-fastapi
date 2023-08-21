import uuid
import time
from models import chats

from sqlalchemy.orm import Session
from DTO.Request import Request



def create_chat(db:Session, req: Request,id: str, time: int):
    db_chat = chats.Chat(version=req.version, message=req.message,
                   room=req.room, user=req.user, chat_id=id,time=time)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat
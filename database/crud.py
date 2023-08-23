import uuid
import time
from models import chats

from sqlalchemy.orm import Session
from DTO.postRequest import postRequest



def create_chat(db:Session, req: postRequest, id: str, time: int):
    db_chat = chats.Chat(version=req.version, message=req.message,
                   room=req.room, user=req.user, chat_id=id,time=time)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

async def update_chat(db:Session, chat_id:str, message: str):
    user = db.query(chats).filter(chats.chat_id == chat_id).first()
    user.message = message
    await db.commit()



def delete_chat(db:Session, chat_id:str):
    query = chats.delete().where(chats.columns.chat_id == chat_id)
    db.execute(query)
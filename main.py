from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from DTO.postRequest import postRequest
from DTO.postRequest import message
from database import connection
from database import crud
from database import redisCrud
from models import chats
from sqlalchemy.orm import Session
import uuid
import time


chats.Base.metadata.create_all(bind=connection.engine)

app = FastAPI()

def get_db():
    db = connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/v1/chats")
async def getchats(roomId: str, db: Session = Depends(get_db)):
    response = {"ok" : True, "msg" : "채팅 조회 성공", "data" : redisCrud.get_chat(roomId)}
    return JSONResponse(content=response)

@app.post("/api/v1/chats")
async def postchats(req: postRequest, db: Session = Depends(get_db)):
    id = str(uuid.uuid4())
    unix = int(time.time())
    crud.create_chat(db,req,id,unix)
    redisCrud.create_chat(req,id,unix)

    return None

@app.get("/api/v1/chats/{chatId}")
async def getOnechats(db: Session = Depends(get_db)):

    return None

@app.patch("/api/v1/chats")
async def updatechats(chatId:str, roodId: str, index:int, req:message, db: Session = Depends(get_db)):
    redisCrud.update_chat(roodId,index,req.message)
    crud.update_chat(db,chatId,message)
    response = {"ok": True, "msg": "채팅 수정 성공"}
    return JSONResponse(content=response)

@app.delete("/api/v1/chats")
async def delchats(chatId:str, roodId: str, index:int, db: Session = Depends(get_db)):
    redisCrud.delete_chat(roodId,index)
    crud.delete_chat(db,chatId)
    return None


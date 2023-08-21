from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from DTO.Request import Request
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
async def postchats(req: Request,db: Session = Depends(get_db)):
    id = str(uuid.uuid4())
    unix = int(time.time())
    crud.create_chat(db,req,id,unix)
    redisCrud.create_chat(req,id,unix)

    return None

@app.get("/api/v1/chats/{chatId}")
async def getOnechats(chatId:str, db: Session = Depends(get_db)):
    return None

@app.patch("/api/v1/chats")
async def updatechats(db: Session = Depends(get_db)):
    return None

@app.delete("/api/v1/chats")
async def delchats(db: Session = Depends(get_db)):
    return None


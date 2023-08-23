from database.redisconfig import redis_config
from DTO.postRequest import postRequest
import json
def create_chat(req: postRequest, id: str, time: int):
    rd = redis_config()
    dic = req.dict()
    dic["chat_id"] = id
    dic["time"] = time
    rd.lpush(req.version+"@test@"+req.room.get("room_id"),json.dumps(dic))
    rd.ltrim(req.version+"@test@"+req.room.get("room_id"),0,99)

def get_chat(room_id: str):
    rd = redis_config()
    jsonString = rd.lrange("v1@test@"+room_id,0,-1)
    jsonString = list(map(json.loads, jsonString))

    return jsonString

def update_chat(room_id:str, index:int, message: str):
    rd = redis_config()
    Data = json.loads(rd.lindex("v1@test@"+room_id, index))
    Data["message"] = message
    rd.lset("v1@test@"+room_id,index,json.dumps(Data))

def delete_chat(room_id:str, index:int):
    rd = redis_config()
    oldData = rd.lindex("v1@test@"+room_id, index)
    newData = oldData.replace("\"message\": "+json.loads(oldData)["message"], "\"message\": \"삭제된 메시지입니다\"")
    rd.lset("v1@test@"+room_id,index,newData)


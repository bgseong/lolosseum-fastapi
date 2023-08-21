from database.redisconfig import redis_config
from DTO.Request import Request
import json
def create_chat( req: Request,id: str, time: int):
    rd = redis_config()
    dic = req.dict()
    dic["chat_id"] = id
    dic["time"] = time
    rd.lpush(req.version+"@test@"+req.room.get("room_id"),json.dumps(dic))
    rd.ltrim(req.version+"@test@"+req.room.get("room_id"),0,99)

def get_chat(room_id: str):
    rd = redis_config()
    jsonString = rd.lrange("v1@test@"+room_id,0,-1)
    for j in jsonString:
        j = json.loads(j)

    return jsonString
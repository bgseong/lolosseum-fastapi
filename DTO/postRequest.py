from pydantic import BaseModel
class postRequest(BaseModel):
    version: str
    message: str
    room: dict
    user: dict

class message(BaseModel):
    message: str
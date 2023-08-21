from pydantic import BaseModel
class Request(BaseModel):
    version: str
    message: str
    room: dict
    user: dict
from pydantic import  BaseModel


class TopicCreate(BaseModel):
    name: str

class TopicResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
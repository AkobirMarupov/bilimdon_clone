from pydantic import BaseModel, EmailStr
from datetime import datetime, date



class QuestionCreateModel(BaseModel):
    title: str
    description: str| None = None
    topic_id: int


class QuestionUpdateModel(BaseModel):
    title: str| None = None
    description: str| None = None
    topic_id: int| None = None


class QuestionResponseModel(BaseModel):
    id: int
    title: int
    description: str | None = None
    topic_id: int 
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
from pydantic import BaseModel, EmailStr
from datetime import datetime, date


class AuthRegistration(BaseModel):
    email: EmailStr
    password: str

class AuthRegistrationResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_staff: bool
    is_superuser: bool

class AuthLogin(BaseModel):
    email: str  
    password: str





class OptionBase(BaseModel):
    title: str
    is_correct: bool

class OptionCreate(OptionBase):
    question_id: int

class OptionUpdate(BaseModel):
    title: str| None = None
    is_correct: bool | None = None

class OptionResponse(OptionBase):
    id: int
    question_id: int
    created_at: datetime

    class Config:
        from_attributes = True



class TopicBase(BaseModel):
    name: str

class TopicCreate(TopicBase):
    pass

class TopicResponse(TopicBase):
    id: int

    class Config:
        from_attributes = True
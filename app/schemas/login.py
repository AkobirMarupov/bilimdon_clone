from pydantic import BaseModel
from datetime import datetime, date


class LoginSchema(BaseModel):
    username: str
    password: str


class SignupSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    birthdate: date
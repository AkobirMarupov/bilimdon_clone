from pydantic import BaseModel



class AuthRegistration(BaseModel):
    email: str
    password: str

class AuthRegistrationResponse(BaseModel):
    id: int
    email: str
    username: str
    is_staff: bool
    is_superuser: bool

class AuthLogin(BaseModel):
    email: str  
    password: str




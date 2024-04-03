from pydantic import BaseModel

class UserRegistration(BaseModel):
    username: str
    password: str
    email: str
    name:str

class UserLogin(BaseModel):
    username: str
    password: str

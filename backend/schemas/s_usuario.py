from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    username: str
    email: str
    password: str

class UsuarioLogin(BaseModel):
    email: str
    password: str
    
    class Config:
        orm_mode = True  
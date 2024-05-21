from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    #     El id se quita porque ya esta instaurado como autoincremento
    id: int | None = None #para que pase un dato vacio
    name: str
    email: str
    password: str
    rol: str 
    

class Ticket(BaseModel):
    #     El id se quita porque ya esta instaurado como autoincremento
    id: int | None = None #para que pase un dato vacio
    desc: str
    date_created: date
    date_last_updated: date
    id_status: int
    id_priority: int
    
class Status(BaseModel):
    id: int | None = None #para que pase un dato vacio
    status: str
    desc: str
    
class Priority(BaseModel):
    id: int | None = None #para que pase un dato vacio
    priority: str

class Logs(BaseModel):
    id: int | None = None #para que pase un dato vacio
    desc : str
    date_new: date
    id_user: int
    id_ticket : int
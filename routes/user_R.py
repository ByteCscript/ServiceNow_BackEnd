from fastapi import APIRouter, Response, status
from config.db import  conn 
from models.user_MOD import users, tickets, status2, priority, logs
from schemas.user_SCH import Logs, User, Ticket, Status, Priority
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet



key = Fernet.generate_key()
f = Fernet(key)

backE = APIRouter()
  
 # EndPoints Usuarios ----------------------------------------------------------
# Obtener Todos los Datos de la BD
@backE.get("/users", response_model=list[User], tags=["Users"])
def get_users():
    return conn.execute(users.select()).fetchall()
     

  # Registrar Datos en la BD
@backE.post("/users", status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(data_user: User):
    new_user = data_user.dict(exclude_none=True)
    new_user["password"] = f.encrypt(data_user.password.encode("utf-8")) # Encriptar contraseña
    conn.execute(users.insert().values(new_user))
    conn.commit()
    
    return "Registration Successfully"

 # Actualización de Usuarios
@backE.put("/users/{ids}", status_code=status.HTTP_426_UPGRADE_REQUIRED, tags=["Users"])
def update_user(ids: int, data_user: User):
    conn.execute(users.update().values(name=data_user.name, email=data_user.email, password=f.encrypt(data_user.password.encode("utf-8"))).where(users.c.id == ids))
    conn.commit()
    
    return "Update"
   

  # Obtencion de Usuarios Individuales
@backE.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=list[User], tags=["Users"])
def get_only_user(id: int):
    result = conn.execute(users.select().where(users.c.id == id))
    return result



 # Eliminacion Individual Usuarios
@backE.delete("/users/{ids}", tags=["Users"])
def delete_user(ids: int):
    conn.execute(users.delete().where(users.c.id == ids))
    conn.commit()
    #return Response(status_code=HTTP_204_NO_CONTENT)
    return "Eliminado"


 # EndPoints Usuarios Fin----------------------------------------------------------



    
 # Endpoints Tickets ---------------------------------------------------------------
 

  # Obtener Todos los Datos de la BD Tickets
@backE.get("/tickets", response_model=list[Ticket], tags=["Ticket"])
def get_tickets():
    return conn.execute(tickets.select()).fetchall()
     

  # Obtencion de Tickets Individuales
@backE.get("/tickets/{ids}", status_code=status.HTTP_200_OK, response_model=list[Ticket], tags=["Ticket"])
def get_only_ticket(ids: int):
    return conn.execute(tickets.select().where(tickets.c.id == ids))
    
     
   # Obtencion de Tickets por Status
@backE.get("/tickets/status/{id_status}", status_code=status.HTTP_200_OK, response_model=list[Ticket], tags=["Ticket"])
def get_all_ticket_only_status(id_status: int):
    return conn.execute(tickets.select().where(tickets.c.id_status == id_status)) # -
    
   # Obtencion de Tickets por Prioridad
@backE.get("/tickets/priority/{id_priority}", status_code=status.HTTP_200_OK, response_model=list[Ticket], tags=["Ticket"])
def get_all_ticket_only_priority(id_priority: int):
    return conn.execute(tickets.select().where(tickets.c.id_priority == id_priority)) # -


   # Ingreso de Tickets
@backE.post("/tickets", status_code=status.HTTP_201_CREATED, tags=["Ticket"])
def create_ticket(data_tic: Ticket):
    new_tic = data_tic.dict(exclude_none=True)
    conn.execute(tickets.insert().values(new_tic))
    conn.commit()
    return "Registration Successfully"

 # Actualización de Tickets
@backE.patch("/tickets/{ids}", status_code=status.HTTP_426_UPGRADE_REQUIRED, tags=["Ticket"])
def update_ticket(ids: int, data_tick: Ticket):
    conn.execute(tickets.update().values(desc=data_tick.desc, date_last_updated=data_tick.date_last_updated, id_status=data_tick.id_status, id_priority=data_tick.id_priority)
                 .where(tickets.c.id == ids))
    conn.commit()
    #result = conn.execute(users.select().where(users.c.id == ids)).first() # revisar porque no trae la consulta **
    return "Update"
   
'''
 # Eliminacion Individual Tickets
@backE.delete("/tickets/{ids}", status_code=status.HTTP_200_OK, tags=["Ticket"])
def delete_tickets(ids: int):
   
    conn.execute(tickets.delete().where(tickets.c.id == ids))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)
    # Funciona si no tiene llaves foraneas
    
    '''
    
 # Endpoints Tickets Fin---------------------------------------------------------------



 # Endpoints Logs ---------------------------------------------------------------


  # Obtener Todos los Datos de la BD Tickets
@backE.get("/status", response_model=list[Status], tags=["Status"])
def get_status():
    return conn.execute(status2.select()).fetchall()
     


@backE.post("/status", status_code=status.HTTP_201_CREATED, tags=["Status"])
def create_status(data_tic: Status):
    new_tic = data_tic.dict(exclude_none=True)
    conn.execute(status2.insert().values(new_tic))
    conn.commit()
   
    return "Registration Successfully"

# Endpoints Logs STATUS---------------------------------------------------------------

@backE.get("/priority", response_model=list[Priority], tags=["Priority"])
def get_priority():
    return conn.execute(priority.select()).fetchall()
    


@backE.post("/priority", status_code=status.HTTP_201_CREATED, tags=["Priority"])
def create_priority(data_tic: Priority):
    new_tic = data_tic.dict(exclude_none=True)
    conn.execute(priority.insert().values(new_tic))
    conn.commit()
    
    return "Registration Successfully"

# Endpoints Logs PRIORITY---------------------------------------------------------------


@backE.get("/logs", response_model=list[Logs], tags=["Logs"])
def get_logs():
    return conn.execute(logs.select()).fetchall()
     


@backE.get("/logs/ticket/{id_ticket}", status_code=status.HTTP_200_OK, response_model=list[Logs], tags=["Logs"])
def get_all_logs_only_ticket(id_ticket: int):
    return conn.execute(logs.select().where(logs.c.id_ticket == id_ticket)) # -
    

@backE.get("/logs/user/{id_user}", status_code=status.HTTP_200_OK, response_model=list[Logs], tags=["Logs"])
def get_all_logs_only_user(id_user: int):
    return conn.execute(logs.select().where(logs.c.id_user == id_user)) # -
    


@backE.post("/logs", status_code=status.HTTP_201_CREATED, tags=["Logs"])
def create_logs(data_tic: Logs):
    new_tic = data_tic.dict(exclude_none=True)
    conn.execute(logs.insert().values(new_tic))
    conn.commit()
   
    return "Registration Successfully"

# Endpoints Logs USERS---------------------------------------------------------------
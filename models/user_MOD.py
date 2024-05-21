from sqlalchemy import ForeignKey, String,Table,Column,DATE,insert
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta,engine,conn

 # Estas tablas crean las verdaderas en MySQL, no requieren de creación anticipada en MariaDB
 # Importante: Tener la conexión establecida en la clase ( db.py ) de manera correcta
      # Tabla Usuarios
users = Table("users", meta, 
              Column("id", Integer, autoincrement=True, primary_key=True), 
              Column("name", String(255)),
              Column("email", String(255)),
              Column("password", String(255), comment="Password User"),
              Column("rol", String(255), nullable=False, comment="Identify Employee Rol")
              )
      # Tabla Prioridad      
priority = Table("priority", meta,
               Column("id", Integer, autoincrement=True, primary_key=True),
               Column("priority", String(255), nullable=False, comment="High, Medium, Low")
               )
      # Tabla Status
status2 = Table("status", meta,
               Column("id", Integer, autoincrement=True, primary_key=True),
               Column("status", String(255), nullable=False, comment="Open, Closed, Fullfilled, In Progress"),
               Column("desc", String(255), nullable=False, comment="Desc of Status () ")
               )
      # Tabla Tickets
tickets = Table("tickets", meta,
                Column("id", Integer, autoincrement=True, primary_key=True),
                Column("desc", String(255), nullable=False),
                Column("date_created", DATE, nullable=False, comment="Ticket Creation Date"),
                Column("date_last_updated", DATE, nullable=False, comment="Ticket last update date"),
                Column("id_priority", Integer, ForeignKey('priority.id'), nullable=False, comment="FK Ticket resolution priority"),
                Column("id_status", Integer, ForeignKey('status.id'), nullable=False, comment="FK Status ticket")
                )
      # Tabla Logs General
logs = Table("logs", meta,
             Column("id", Integer, autoincrement=True, primary_key=True),
             Column("desc", String(255), nullable=False, comment="Descripcion log"),
             Column("date_new", DATE, nullable=False, comment="Date Modify Comment"),
             Column("id_user", Integer, ForeignKey('users.id'), nullable=False, comment="ID of the Users" ),
             Column("id_ticket", Integer, ForeignKey('tickets.id'), nullable=False, comment="ID of the Tickets")
             )


# Ejemplo para insertar datos en el swagger mas no en MySQL
'''
conn.execute(
    insert(users),
    [
        {"name": "spongebob", "email": "Spongebob@gmail.com", "password": "Halo123+", "rol": 2},
        {"name": "Johan Gil", "email": "johangilc@gmail.com", "password": "Pepito125+-", "rol": 1},
        {"name": "Randy Caballero", "email": "randynova@gmail.com", "password": "trund78+*-", "rol": 4},
        {"name": "Luis Castro", "email": "lui@copnia.com", "password": "limaPeru", "rol": 6},
        {"name": "John 117", "email": "john@hotmail.com", "password": "++Renualt123", "rol": 3},
    ],
)
'''

'''
conn.execute(
    insert(status2),
    [
        {"status": "Open", "desc" : "El ticket aun no se ha solucionado" },
        {"status": "In Progress", "desc" : "El ticket se encuentra en progreso" },
        {"status": "Fullfilled", "desc" : "El ticket se encuentra Completado" },
        {"status": "Closed", "desc" : "El ticket se ha cerrado" }
    ],
)
'''

meta.create_all(engine)
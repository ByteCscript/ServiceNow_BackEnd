from fastapi import FastAPI
from routes.user_R import backE


app = FastAPI(
    title="FastAPI - ServiceNow_RJ",
    description="BackEnd API - ServiceNow, \n - Randy Caballero \n - Johan Gil",
    version="0.0.1",
  
)

app.include_router(backE)
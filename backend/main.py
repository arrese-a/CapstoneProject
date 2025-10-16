import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json 
from config.database import engine, Base
from endpoints import recetas_api, lista_compra_api, sesiones_api, favoritas_api
app = FastAPI()

Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://capstoneproject-front.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recetas_api.router, prefix="/recetas", tags=["Recetas"])
app.include_router(sesiones_api.router, prefix="/sesion", tags=["Sesiones"])
app.include_router(lista_compra_api.router, prefix="/lista-compra", tags=["ListaCompra"])
app.include_router(favoritas_api.router, prefix="/favoritas", tags=["Favoritas"])
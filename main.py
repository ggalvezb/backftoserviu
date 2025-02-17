from fastapi import FastAPI
#from fastapi.staticfiles import StaticFiles
from routers import FTO
from routers import Proyecto
from routers import Administrador
# Inicia el servidor: uvicorn main:app --reload

app=FastAPI()

#routers
app.include_router(FTO.router)
app.include_router(Proyecto.router)
app.include_router(Administrador.router)
@app.get("/")
async def root():
    return{"message":"Hello World"}
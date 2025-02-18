from fastapi import FastAPI
#from fastapi.staticfiles import StaticFiles
from routers import FTO
from routers import Proyecto
from routers import Administrador
from fastapi.middleware.cors import CORSMiddleware
# Inicia el servidor: uvicorn main:app --reload

app=FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar dominios en lugar de "*" para mayor seguridad
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados HTTP
)

#routers
app.include_router(FTO.router)
app.include_router(Proyecto.router)
app.include_router(Administrador.router)
@app.get("/")
async def root():
    return{"message":"Hello World"}
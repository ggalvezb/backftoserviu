from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.Proyectos import Proyecto
from db.schemas.Proyectos import proyecto_schema, proyectos_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/proyecto",tags=["Proyecto"])
registro_bd=db_client.proyecto

#Retorno todos los entidadpatrocinante
@router.get("/", response_model=list[Proyecto])
async def proyecto():
    return fun.retorno_todos_perfiles(proyectos_schema,registro_bd)

#Agrego un entidadpatrocinante a la BD
@router.post("/")
async def proyecto(beneficiario:Proyecto):
    return fun.agrego_registro(Proyecto,proyecto_schema,beneficiario,"id",beneficiario.id,registro_bd)

#Elimino un entidadpatrocinante de la BD
@router.delete("/{id}")
async def proyecto(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))


@router.put("/", response_model=Proyecto,description="Esta funcion edita el proyecto por ID")
async def proyecto(proyecto:Proyecto):
    registro_dict=dict(proyecto)
    del registro_dict["id"]
    try:
        registro_bd.find_one_and_replace({"_id": ObjectId(proyecto.id)}, registro_dict)
    except:
        return {"Error: No se a encontrado usuario"}
    return proyecto






#Edito un campo de una entidadpatrocinante en la BD
#@router.put("/", response_model=Proyecto,description="Esta funcion Edita por ID")
#async def proyecto(beneficiario:Proyecto):
#    return fun.edito_registro(Proyecto,proyecto_schema,beneficiario,"_id",beneficiario.id,registro_bd)
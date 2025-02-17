from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.FTO import FTO
from db.schemas.FTO import fto_schema, ftos_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/fto",tags=["FTO"])
registro_bd=db_client.fto

#Retorno todos los fto
@router.get("/", response_model=list[FTO])
async def fto():
    return fun.retorno_todos_perfiles(ftos_schema,registro_bd)

#Agrego un fto a la BD
@router.post("/")
async def fto(beneficiario:FTO):
    return fun.agrego_registro(FTO,fto_schema,beneficiario,"id",beneficiario.id,registro_bd)

#Elimino un fto de la BD
@router.delete("/{id}")
async def fto(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

@router.put("/", response_model=FTO,description="Esta funcion edita el proyecto por ID")
async def proyecto(proyecto:FTO):
    registro_dict=dict(proyecto)
    del registro_dict["id"]
    try:
        registro_bd.find_one_and_replace({"_id": ObjectId(proyecto.id)}, registro_dict)
    except:
        return {"Error: No se a encontrado usuario"}
    return proyecto

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from db.client import db_client
from db.models.Admin import Administrador
from db.schemas.Admin import admin_schema, admins_schema
from bson import ObjectId
import routers.funciones as fun
#from routers.auth_user import oauth2

router=APIRouter(prefix="/administrador",tags=["Administrador"])
registro_bd=db_client.administrador

#Retorno todos los fto
@router.get("/", response_model=list[Administrador])
async def fto():
    return fun.retorno_todos_perfiles(admins_schema,registro_bd)

#Agrego un fto a la BD
@router.post("/")
async def fto(beneficiario:Administrador):
    return fun.agrego_registro(Administrador,admin_schema,beneficiario,"id",beneficiario.id,registro_bd)

#Elimino un fto de la BD
@router.delete("/{id}")
async def fto(id: str):
    return fun.elimino_registro(registro_bd,ObjectId(id))

#Edito un campo de una fto en la BD
@router.put("/", response_model=Administrador,description="Esta funcion busca por usuario_id")
async def fto(beneficiario:Administrador):
    return fun.edito_registro(Administrador,admin_schema,beneficiario,"usuario_id",beneficiario.usuario_id,registro_bd)
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

# Asigno Proyecto a FTO
@router.put("/asignarProyecto/{id_fto}/{id_proyecto}", response_model=FTO, description="Esta funcion asigna un proyecto a un FTO, en caso de que el proyecto ya este asignado a otro FTO, se desasigna de este. \n En caso de que el proyecto ya este asignado al FTO, se retorna un error")
async def asignarProyecto(id_fto: str, id_proyecto: str):
    try:
        fto = registro_bd.find_one({"_id": ObjectId(id_fto)})
        if fto is None:
            raise HTTPException(status_code=404, detail="FTO no encontrado")

        proyecto = db_client.proyecto.find_one({"_id": ObjectId(id_proyecto)})
        if proyecto is None:
            raise HTTPException(status_code=404, detail="Proyecto no encontrado")
        
        #Chequeo si el proyecto ya esta asignado al FTO
        if id_proyecto in fto["proyectos"]:
            raise HTTPException(status_code=400, detail="Proyecto ya asignado al FTO")

        
        #Chequeo si el proyecto esta asignado a otro FTO y lo desasigno
        for fto_id in registro_bd.find({}, {"_id": 1}):
            fto_id = str(fto_id["_id"])
            if id_proyecto in registro_bd.find_one({"_id": ObjectId(fto_id)})["proyectos"]:
                registro_bd.find_one_and_update({"_id": ObjectId(fto_id)}, {"$pull": {"proyectos": id_proyecto}})


        fto["proyectos"].append(id_proyecto)
        result = registro_bd.find_one_and_replace({"_id": ObjectId(id_fto)}, fto, return_document=True)
        if result is None:
            raise HTTPException(status_code=500, detail="Error al actualizar el FTO")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    result["id"] = str(result["_id"])
    return result

    
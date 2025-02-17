from pydantic import BaseModel,EmailStr, Field
from typing import Optional,List
from bson import ObjectId

#Entidad psat
class FTO(BaseModel):
    id: Optional[str]
    nombre:str
    correo:str
    clave:str
    proyectos:Optional[list]



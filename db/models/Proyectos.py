from pydantic import BaseModel,EmailStr, Field
from typing import Optional,List
from bson import ObjectId

#Entidad psat
class Proyecto(BaseModel):
    id: Optional[str]
    id_fto: Optional[str]
    NOMBRE_FTO: Optional[str]
    NOMBRE_PROYECTO:Optional[str]
    CODIGO:Optional[str]
    DIRECCION:Optional[str]
    COMUNA:Optional[str]
    ENTIDAD_PATROCINANTE:Optional[str]
    FECHA_INICIO:Optional[str]
    FECHA_TERMINO_PROGRAMADA:Optional[str]
    PLAZO_EJECUCION_DE_OBRAS:Optional[str]
    FECHA_VIGENCIA_GARANTIA_CTTO_EC:Optional[str]
    PLAZO_EJECUCION_DE_CCTTO_FTO:Optional[str]
    FECHA_VIGENCIA_GARANTIA_CTTO_FTO:Optional[str]
    PORCENTAJE_DE_AVANCE_REAL_SEMANAL_ACTUAL:Optional[str]
    PORCENTAJE_DE_AVANCE_REAL_ACUMULADO_A_LA_FECHA:Optional[str]
    PORCENTAJE_DE_AVANCE_REAL_HISTORICO:Optional[list]
    PORCENTAJES_DE_AVANCE_PROGRAMADO:Optional[list]
    CERTIFIACIONES_PARA_OBTENCIÓN_DE_RECEPCION_FINAL:Optional[list]
    N_DE_INGRESO_DE_DOCUMENTACION:Optional[list]
    FECHA_DE_INGRESO_DE_DOCUMENTACION:Optional[list]
    PLAZO_NORMATIVO_ASOCIADO_A_CERTIFICACION:Optional[list]
    OBSERVACIONES:Optional[list]



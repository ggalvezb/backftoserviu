def proyecto_schema(proyecto) -> dict:
    return {"id": str(proyecto["_id"]),
            "id_fto": str(proyecto["id_fto"]),
            "NOMBRE_FTO": str(proyecto["NOMBRE_FTO"]),
            "NOMBRE_PROYECTO":str(proyecto["NOMBRE_PROYECTO"]),
            "CODIGO":str(proyecto["CÓDIGO"]),
            "DIRECCION":str(proyecto["DIRECCION"]),
            "COMUNA":str(proyecto["COMUNA"]),
            "ENTIDAD_PATROCINANTE":str(proyecto["ENTIDAD_PATROCINANTE"]),
            "FECHA_INICIO":str(proyecto["FECHA_INICIO"]),
            "FECHA_TERMINO_PROGRAMADA":str(proyecto["FECHA_TERMINO_PROGRAMADA"]),
            "PLAZO_EJECUCION_DE_OBRAS":str(proyecto["PLAZO_EJECUCION_DE_OBRAS"]),
            "FECHA_VIGENCIA_GARANTIA_CTTO_EC":str(proyecto["FECHA_VIGENCIA_GARANTIA_CTTO_EC"]),
            "PLAZO_EJECUCION_DE_CCTTO_FTO":str(proyecto["PLAZO_EJECUCION_DE_CCTTO_FTO"]),
            "FECHA_VIGENCIA_GARANTIA_CTTO_FTO":str(proyecto["FECHA_VIGENCIA_GARANTIA_CTTO_FTO"]),
            "PORCENTAJE_DE_AVANCE_REAL_SEMANAL_ACTUAL":str(proyecto["PORCENTAJE_DE_AVANCE_REAL_SEMANAL_ACTUAL"]),
            "PORCENTAJE_DE_AVANCE_REAL_ACUMULADO_A_LA_FECHA":str(proyecto["PORCENTAJE_DE_AVANCE_REAL_ACUMULADO_A_LA_FECHA"]),
            "PORCENTAJE_DE_AVANCE_REAL_HISTORICO":list(proyecto["PORCENTAJE_DE_AVANCE_REAL_HISTORICO"]),
            "PORCENTAJES_DE_AVANCE_PROGRAMADO":list(proyecto["PORCENTAJES_DE_AVANCE_PROGRAMADO"]),
            "CERTIFIACIONES_PARA_OBTENCIÓN_DE_RECEPCION_FINAL":list(proyecto["CERTIFIACIONES_PARA_OBTENCIÓN_DE_RECEPCION_FINAL"]),
            "N_DE_INGRESO_DE_DOCUMENTACION":list(proyecto["N_DE_INGRESO_DE_DOCUMENTACION"]),
            "FECHA_DE_INGRESO_DE_DOCUMENTACION":list(proyecto["FECHA_DE_INGRESO_DE_DOCUMENTACION"]),
            "PLAZO_NORMATIVO_ASOCIADO_A_CERTIFICACION":list(proyecto["PLAZO_NORMATIVO_ASOCIADO_A_CERTIFICACION"]),
            "OBSERVACIONES":list(proyecto["OBSERVACIONES"]),
    }

#test
def proyectos_schema(proyectos) -> list:
    return [proyecto_schema(proyecto) for proyecto in proyectos]

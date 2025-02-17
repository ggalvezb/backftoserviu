def fto_schema(fto) -> dict:
    return {"id": str(fto["_id"]),
            "nombre": str(fto["nombre"]),
            "correo": str(fto["correo"]),
            "clave": str(fto["clave"]),
            "proyectos": list(fto["proyectos"]),

    }

def ftos_schema(ftos) -> list:
    return [fto_schema(fto) for fto in ftos]

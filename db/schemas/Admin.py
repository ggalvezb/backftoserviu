def admin_schema(admin) -> dict:
    return {"id": str(admin["_id"]),
            "nombre": str(admin["nombre"]),
            "correo": str(admin["correo"]),
            "clave": str(admin["clave"]),
            "proyectos": list(admin["proyectos"]),

    }

def admins_schema(admins) -> list:
    return [admin_schema(admin) for admin in admins]

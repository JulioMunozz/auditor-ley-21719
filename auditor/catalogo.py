"""Catálogo de datos personales: palabras clave en nombres de columna -> (tipo, categoría)."""

CATALOGO = {
    # Datos personales
    "nombre": ("Nombre", "Personal"),
    "rut": ("RUT", "Personal"),
    "run": ("RUT", "Personal"),
    "correo": ("Correo", "Personal"),
    "email": ("Correo", "Personal"),
    "mail": ("Correo", "Personal"),
    "telefono": ("Teléfono", "Personal"),
    "fono": ("Teléfono", "Personal"),
    "celular": ("Teléfono", "Personal"),
    "direccion": ("Dirección", "Personal"),
    "domicilio": ("Dirección", "Personal"),
    "nacimiento": ("Fecha de nacimiento", "Personal"),
    "genero": ("Género", "Personal"),
    "sexo": ("Género", "Personal"),
    "civil": ("Estado civil", "Personal"),
    "ip": ("Dirección IP", "Personal"),
    "patente": ("Patente", "Personal"),
    "cuenta": ("Cuenta bancaria", "Personal"),
    "bancaria": ("Cuenta bancaria", "Personal"),
    "sueldo": ("Remuneración", "Personal"),
    "salario": ("Remuneración", "Personal"),
    "remuneracion": ("Remuneración", "Personal"),
    # Datos sensibles
    "salud": ("Salud", "Sensible"),
    "diagnostico": ("Salud", "Sensible"),
    "enfermedad": ("Salud", "Sensible"),
    "sindicato": ("Afiliación sindical", "Sensible"),
    "sindical": ("Afiliación sindical", "Sensible"),
    "etnia": ("Origen étnico", "Sensible"),
    "religion": ("Creencia religiosa", "Sensible"),
    "huella": ("Dato biométrico", "Sensible"),
    "biometrico": ("Dato biométrico", "Sensible"),
}


def detectar_por_nombre(nombre_columna):
    """Devuelve (tipo, categoría) si el nombre de la columna está en el catálogo, o None."""
    palabras = nombre_columna.lower().split("_")
    for palabra in palabras:
        if palabra in CATALOGO:
            return CATALOGO[palabra]
    return None
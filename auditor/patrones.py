"""Patrones para detectar datos personales en un texto."""

import re

from rut import validar_rut

PATRON_RUT = re.compile(r"^((\d{1,2}\.)?\d{3}\.\d{3}|\d{6,8})-[\dkK]$")
PATRON_CORREO = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")
PATRON_TELEFONO = re.compile(r"^\+56\s?9\s?\d{4}\s?\d{4}$")


def detectar_valor(texto):
    """Devuelve 'RUT', 'Correo', 'Telefono' o None según lo que parezca el texto."""
    if not isinstance(texto, str):
        return None

    texto = texto.strip()

    if PATRON_RUT.match(texto) and validar_rut(texto):
        return "RUT"
    if PATRON_CORREO.match(texto):
        return "Correo"
    if PATRON_TELEFONO.match(texto):
        return "Telefono"
    return None
PALABRAS_CLAVE = {
    "RUT": ["rut", "run"],
    "Correo": ["email", "correo", "mail"],
    "Telefono": ["telefono", "fono", "celular", "phone"],
}


def detectar_columna(nombre):
    """Devuelve 'RUT', 'Correo', 'Telefono' o None según el nombre de la columna."""
    nombre = nombre.lower()
    for tipo, palabras in PALABRAS_CLAVE.items():
        for palabra in palabras:
            if palabra in nombre:
                return tipo
    return None
def enmascarar(valor, tipo):
    """Oculta parte de un dato personal para mostrarlo sin exponerlo."""
    valor = str(valor).strip()
    if tipo == "Correo" and "@" in valor:
        usuario, dominio = valor.split("@", 1)
        return usuario[0] + "***@" + dominio
    if len(valor) <= 4:
        return "*" * len(valor)
    if tipo == "RUT":
        return valor[:2] + "*" * (len(valor) - 3) + valor[-1]
    # Telefono y cualquier otro: deja el inicio y los últimos 4 caracteres
    return valor[:3] + "*" * (len(valor) - 7) + valor[-4:]
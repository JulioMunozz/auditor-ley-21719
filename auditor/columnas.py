"""Análisis de una columna completa para decidir qué tipo de dato personal contiene."""

from auditor.catalogo import detectar_por_nombre
from auditor.patrones import detectar_valor


UMBRAL = 60  # porcentaje mínimo de valores que deben calzar para marcar la columna


def analizar_columna(serie):
    """Devuelve el tipo más frecuente, el porcentaje que calza y si la columna se marca."""
    # 1. Quitar los valores vacíos y pasar todo a texto
    valores = serie.dropna().astype(str)
    valores = valores[valores.str.strip() != ""]

    # 2. Si no quedó nada, devolver un resultado vacío
    if valores.empty:
        return {"tipo": None, "porcentaje": 0.0, "marcada": False}

    # 3. Aplicar detectar_valor a cada valor y quedarse solo con los que calzaron
    tipos = valores.apply(detectar_valor).dropna()

    if tipos.empty:
        return {"tipo": None, "porcentaje": 0.0, "marcada": False}

    # 4. El tipo más frecuente y su porcentaje sobre el total de valores no vacíos
    tipo = tipos.value_counts().idxmax()
    porcentaje = float(round((tipos == tipo).sum() / len(valores) * 100, 1))

    return {"tipo": tipo, "porcentaje": porcentaje, "marcada": porcentaje >= UMBRAL}

# Los tipos de detectar_valor escritos como en el catálogo
NOMBRES_TIPO = {"RUT": "RUT", "Correo": "Correo", "Telefono": "Teléfono"}


def auditar_columna(nombre, serie):
    """Combina la detección por valores y por nombre. Devuelve el hallazgo o None."""
    por_valor = analizar_columna(serie)
    por_nombre = detectar_por_nombre(nombre)

    detecto_valor = por_valor["marcada"]
    detecto_nombre = por_nombre is not None

    if not detecto_valor and not detecto_nombre:
        return None  # ninguna de las dos detectó algo: no es hallazgo

    if detecto_valor and detecto_nombre:
        detectado_por = "valor y nombre"
    elif detecto_valor:
        detectado_por = "valor"
    else:
        detectado_por = "nombre"

    if detecto_nombre:
        tipo, categoria = por_nombre
    else:
        tipo, categoria = NOMBRES_TIPO[por_valor["tipo"]], "Personal"

    return {
        "columna": nombre,
        "tipo": tipo,
        "categoria": categoria,
        "porcentaje": por_valor["porcentaje"],
        "detectado_por": detectado_por,
    }
"""Análisis de una columna completa para decidir qué tipo de dato personal contiene."""

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
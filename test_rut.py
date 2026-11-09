from rut import validar_rut


def test_rut_valido_con_puntos():
    assert validar_rut("12.345.678-5") == True


def test_rut_valido_sin_puntos():
    assert validar_rut("12345678-5") == True


def test_rut_con_k_minuscula():
    assert validar_rut("11.111.112-k") == True


def test_rut_con_dv_incorrecto():
    assert validar_rut("12.345.678-9") == False


def test_texto_vacio():
    assert validar_rut("") == False


def test_valor_que_no_es_texto():
    assert validar_rut(12345678) == False
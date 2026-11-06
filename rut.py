"""Validación de RUT chileno con el algoritmo módulo 11."""
 
 
def calcular_dv(cuerpo):
    """Calcula el dígito verificador de un cuerpo de RUT (solo números)."""
    suma = 0
    for i, digito in enumerate(reversed(cuerpo)):
        multiplicador = 2 + (i % 6)  # 2, 3, 4, 5, 6, 7, 2, 3...
        suma += int(digito) * multiplicador
 
    resultado = 11 - (suma % 11)
    if resultado == 11:
        return "0"
    if resultado == 10:
        return "K"
    return str(resultado)
 
 
def validar_rut(rut):
    """Devuelve True si el RUT tiene un dígito verificador correcto."""
    if not isinstance(rut, str):
        return False
 
    limpio = rut.replace(".", "").replace("-", "").strip().upper()
    if len(limpio) < 2:
        return False
 
    cuerpo, dv = limpio[:-1], limpio[-1]
    if not cuerpo.isdigit():
        return False
 
    return calcular_dv(cuerpo) == dv
 
 
if __name__ == "__main__":
    from faker import Faker
 
    fake = Faker("es_CL")
    Faker.seed(42)
 
    print("RUT generados por Faker (deberían ser True):")
    for _ in range(5):
        rut = fake.rut()
        print(f"  {rut:>14} -> {validar_rut(rut)}")
 
    print("\nRUT mal escritos (deberían ser False):")
    for rut in ["12.345.678-9", "11.111.111-K"]:
        print(f"  {rut:>14} -> {validar_rut(rut)}")
 
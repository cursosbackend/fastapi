
def calcular_estadisticas(notas:list[float]) -> dict :
    """calcula las estadisticas de una lista de notas"""
    try:
        promedio = sum(notas) / len(notas)
        mayor = max(notas)
        menor = min(notas)
        aprobado = [a for a in notas if a >= 4.0]

        resultado = {
            "promedio": promedio,
            "mayor"   : mayor,
            "menor"   : menor,
            "aprobado": aprobado
        }
        return resultado
    except ZeroDivisionError:
        return None











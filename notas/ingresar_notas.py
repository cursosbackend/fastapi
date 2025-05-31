
def ingresar_notas() -> list[float]:
    """
    solicita al usuario ingresar  notas separadas por espacio,
    se separan y se transforman en una lista de flotantes
    """

    n = input("ingresa las notas (el formato debe ser separado por espacio (7.0 8.0 6.7))")
    n = n.split(" ")
    notas = [float(nota) for nota in n]
    return notas




def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado su lado.
    :param lado: Lado del cuadrado
    :return: Área del cuadrado
    """
    area = lado * lado
    return area

lado_cuadrado = [1,3,4]
area_cuadrado = []

for lado in lado_cuadrado:
    area = calcular_area_cuadrado(lado)
    area_cuadrado.append(area)
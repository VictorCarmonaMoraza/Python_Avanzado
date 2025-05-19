def calcular_perimetro(*args):
    print(f'es una tupla con cada uno de los parametros que mandamos a la funcion {args}')
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro


perimetro = calcular_perimetro(10, 20, 30, 40)
print(f"El perimetro es: {perimetro}")



tringulo = calcular_perimetro(10, 20, 30)
print(f"El perimetro del triangulo es: {tringulo}")
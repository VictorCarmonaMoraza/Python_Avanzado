
def funcion_kwars(**kwargs):
    print(f'kwargs es un diccionario {kwargs}')
    for llave, valor in kwargs.items():
        print(f'Llave: {llave} - Valor: {valor}')
    print(kwargs["nombre"], kwargs["edad"], kwargs["ciudad"])

"""Llamada a la funcion con un diccionario como argumento"""
funcion_kwars(nombre='Juan', edad=30, ciudad='Madrid')

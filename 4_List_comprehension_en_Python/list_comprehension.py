
"""
lista = [ expresion(elemento) for elemento in objeto_iterable]
"""

def calcular_cuadrado(numero):
    return numero ** 2

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_cuadrados = []

for num in lista_num:
    cuadrado = num ** 2
    lista_cuadrados.append(cuadrado)


print("Ciclo for", lista_cuadrados) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(f'----------------')

lista_comprehension = [num ** 2 for num in lista_num]
print("Lista comprehension", lista_comprehension) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(f'----------------')
lista_comprehension2 = [calcular_cuadrado(num) for num in lista_num]
print("Lista comprehension_2", lista_comprehension2) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

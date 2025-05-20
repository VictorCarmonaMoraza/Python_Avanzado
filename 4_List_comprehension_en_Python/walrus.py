
def calcular_cuadrado(numero):
    """Calcular el cuadrado de un numero"""
    return numero ** 2

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares =[]

for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    if num % 2 == 0:
        lista_pares.append(cuadrado)
        print(f'El cuadrado de {num} es {cuadrado}, es un numero par')
    else:
        print(f'El cuadrado de {num} es {cuadrado}, es un numero impar')

print(f'-------SECCION WALRUS---------')
lista_pares_WALRUS = []
# Con walrus operador desde las version 3.0 de python
for num in lista_num:
    #cuadrado = calcular_cuadrado(num)
    if (cuadrado := calcular_cuadrado(num)) % 2 == 0:
        lista_pares_WALRUS.append(cuadrado)
        #print(f'El cuadrado de {num} es {cuadrado}, es un numero par')
    #else:
        #print(f'El cuadrado de {num} es {cuadrado}, es un numero impar')
print(lista_pares_WALRUS)


print(f'-------SECCION WALRUS_2---------')
pares_comprehension = [cuadrado for num in lista_num if (cuadrado := calcular_cuadrado(num)) % 2 == 0]
print(pares_comprehension)

def calcular_cuadrado(numero):
   ##Calcular el cuadrado de un numero 
    return numero ** 2

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []

for num in lista_num:
    ##Por cada numero de la lista, calcular el cuadrado
    cuadrado = calcular_cuadrado(num)
    ##Agregar el cuadrado a la lista
    lista_cuadrados.append(cuadrado)

# Imprimir la lista de cuadrados
print(lista_cuadrados) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


print(f'----------------')


##Utilizar map para reemplazra el ciclo for
lista_num2 = [1,2,3,4,5,6,7,8,9,10]

map_cuadrados = map(calcular_cuadrado, lista_num2)
print(list(map_cuadrados)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
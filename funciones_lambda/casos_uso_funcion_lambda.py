
lista_numeros= [1,2,3,4,5,6,7,8]

lista_pares = lambda numero:numero % 2 == 0

print(lista_pares(2)) # True
print(lista_pares(3)) # False

# Usando la función filter para filtrar números pares
lista_pares2 = list(filter(lambda numero: numero % 2 == 0, lista_numeros))
print(lista_pares2) # [2, 4, 6, 8]

# Usando la función map para elevar al cuadrado los números de la lista
nueva_lista = map(lambda numero:numero*10, lista_numeros)
print(list(nueva_lista)) # [10, 20, 30, 40, 50, 60, 70, 80]


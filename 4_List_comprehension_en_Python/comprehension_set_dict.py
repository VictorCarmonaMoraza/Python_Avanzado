
lista_num = [1, 2, 2, 3, 4, 5, 6, 7, 8]

#Creacion de un set comprehension
#Los set no contienen elementos repetidos
##No ordenado: Los elementos en un set no tienen una posición fija
#  ni un índice. No puedes acceder a los elementos de un set utilizando
#  un índice como lo harías con una lista o una tupla

set_pares = {num for num in lista_num if num % 2 == 0}
print(set_pares) # {2, 4, 6, 8}
print(f'----------------')


#Creacion de un diccionario comprehension
vocales = "aeiou"
diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(diccionario) # {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}
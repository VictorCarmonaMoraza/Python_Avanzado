
# Creamos una lista de números
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Objeto iterador
iterador = iter(lista_numeros)

# imprimimos el ietardor
#print(iterador) # <list_iterator object at 0x7f8c1c2e3d90>

print(next(iterador)) # 1
print(next(iterador)) # 2
print(next(iterador)) # 3

print(f'----------------')
##ecorrer las lista de iteradores
## Imprime desde el 4 porque ya imprimiste el valor 3
for numero in iterador:
    print(numero) # 4, 5, 6, 7, 8


'''
enumerate(iterable, start=0) -> iterator
'''

nombres =['Juan', 'Pedro', 'Maria', 'Ana']

# Enumerar la lista
nombres_enumerados = enumerate(nombres)
print(list(nombres_enumerados)) # [(1, 'Juan'), (2, 'Pedro'), (3, 'Maria'), (4, 'Ana')]


print(f'----------------')


nombres_enumerados = enumerate(nombres, start=5)
print(list(nombres_enumerados)) # [(5, 'Juan'), (6, 'Pedro'), (7, 'Maria'), (8, 'Ana')]


print(f'--------CICLO FOR--------')
# Enumerar la lista con un ciclo for
for indice, elemento in enumerate(nombres):
    print(f'Indice: {indice}, Nombre: {elemento}')

lista_nombres = ['Juan', 'Pedro', 'Maria', 'Ana']

# Ciclo for con else
for nombre in lista_nombres:
    print(nombre)
    if nombre == 'Maria':
        break
else:
    print('No hay más nombres en la lista')

nombrea= ['Juan', 'Pedro', 'Maria']
apellidos = ['Pérez', 'Gómez', 'López']


nombre_completo =zip(nombrea, apellidos)
print(list(nombre_completo))

print(f'----------------')

#Unir listas
for nombre, apellido in zip(nombrea, apellidos):
    print(f'{nombre} {apellido}')

print(f'----------------')
nombres_unzip,apellidos_unzip = zip(*zip(nombrea, apellidos))
print(nombres_unzip) # ('Juan', 'Pedro', 'Maria')
print(apellidos_unzip) # ('Pérez', 'Gómez', 'López')


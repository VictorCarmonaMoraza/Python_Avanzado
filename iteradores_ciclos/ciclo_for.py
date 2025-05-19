
nombres_list = ['Juan', 'Pedro', 'Maria', 'Ana']
for nombre in nombres_list:
    print(nombre)


print(f'----------------')
#Imprime Juan y Pedro
for nombre in nombres_list:
    if nombre == 'Maria':
        #Se para y no itera sobre los siguientes elementos
        break
    print(nombre) 

print(f'----------------')
#No imprirme Maria la pasa de largo
for nombre in nombres_list:
    if nombre == 'Maria':
        #Se imprime todo lo que sea diferente a Maria
        continue
    print(nombre) 


print(f'----------------')
#No imprirme nada ya que nos estamos saltado todos los nombres
for nombre in nombres_list:
    continue
    print(nombre)
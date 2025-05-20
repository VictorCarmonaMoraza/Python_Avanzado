
'''
range(incio,fin,paso)
'''
#El 5 no es inclusivo y es el fin
serie_1 =range(5)
print(serie_1) # range(0, 5)
print(list(serie_1)) # range(0, 5)


print(f'----------------')
#El 10 no es inclusivo y esle fin
serie_2 = range(5, 10)
print(serie_2) # range(5, 10)
print(list(serie_2)) # range(5, 10)


print(f'----------------')

serie_3 = range(3, 10, 2)
print(serie_3) # range(3, 10, 2)
print(list(serie_3)) # range(3, 10, 2)

print(f'-------CICLO FOR---------')
for elemento in serie_3:
    print(elemento) # 3, 5, 7, 9
import csv
with open("datos2.csv", "r", encoding="utf-8") as archivo:
    #lector de nuestro archivo que pasa por las filas y obtiene informacion
    reader = csv.reader(archivo, delimiter=",")
    #Nos permite salta la primera fila
    columnas = next(reader)
    print("Columnas:",columnas)
    #Ciclo for
    for fila in reader:
        print(fila[0])



print("-------DICTIONAIO--------")
with open("datos2.csv", "r", encoding="utf-8") as archivo:
    #lector de nuestro archivo que pasa por las filas y obtiene informacion
    reader = csv.DictReader(archivo, delimiter=",")
    #Nos permite salta la primera fila
    #columnas = next(reader)
    #print("Columnas:",columnas)
    #Ciclo for
    for fila in reader:
        print(fila["nombre"])
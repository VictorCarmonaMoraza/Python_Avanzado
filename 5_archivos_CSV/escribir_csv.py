import csv

columnas = ["nombre","apellido","edad"]
dato = ["Pâco","Botero",26]

datos_lista = [
    ["Pâco","Botero",26],
    ["Juan","Gomez",30],
    ["Maria","Lopez",22],
    ["Ana","Torres",28],
    ["Luis","Martinez",35]
]

datos_dict = [
    {"nombre":"Pâco","apellido":"Botero","edad":26},
    {"nombre":"Juan","apellido":"Gomez","edad":30},
    {"nombre":"Maria","apellido":"Lopez","edad":22},
    {"nombre":"Ana","apellido":"Torres","edad":28},
    {"nombre":"Luis","apellido":"Martinez","edad":35}
]

#newline es para que no se agregue un salto de linea al final del archivo
#encoding es para que no se agregue un error de codificacion
with open("datos.csv","w", encoding="utf-8", newline="") as archivo:
    writer = csv.writer(archivo, delimiter=",")
    # Escribir la cabecera
    writer.writerow(columnas)
    # Escribir los datos
    writer.writerow(dato)


print("---------------")
#newline es para que no se agregue un salto de linea al final del archivo
#encoding es para que no se agregue un error de codificacion
with open("datos2.csv","w", encoding="utf-8", newline="") as archivo:
    writer = csv.writer(archivo, delimiter=",")
    # Escribir la cabecera
    writer.writerow(columnas)
    # Escribir los datos
    writer.writerows(datos_lista)


print("-------DICTIONAIO--------")
#newline es para que no se agregue un salto de linea al final del archivo
#encoding es para que no se agregue un error de codificacion
with open("datos_dict.csv","w", encoding="utf-8", newline="") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=columnas, delimiter=",")
    writer.writeheader()
    # Escribir los datos
    writer.writerows(datos_dict)

import csv
import os

#ruta donde se guardara nuestro csv
ruta_relativa ="csv_vacio.csv"
ruta_absoluta ="C:\\Users\\Victo\\Desktop\\DataCience\\PYTHON_BASIC\\5_archivos_CSV\\csv_vacio.csv"


##Definir la ruta absoulta mediante os
ruta_absoulta_os = os.path.join(os.getcwd(),"csv_vacio.csv")

print(f'ruta de manera tradicional: {ruta_absoluta}')
print(f'ruta obtenida mediante ka importacion de os: {ruta_absoulta_os}')
#abrimos el archivo en modo escritura
#archivo_abierto = open(ruta,"w")

#creamos el objeto writer
#writer = csv.writer(archivo_abierto, delimiter=",")

#Cerrar el archivo
#archivo_abierto.close()


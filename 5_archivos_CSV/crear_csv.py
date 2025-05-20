
import csv

#ruta donde se guardara nuestro csv
ruta ="csv_vacio.csv"

#abrimos el archivo en modo escritura
archivo_abierto = open(ruta,"w")

#creamos el objeto writer
writer = csv.writer(archivo_abierto, delimiter=",")

#Cerrar el archivo
archivo_abierto.close()


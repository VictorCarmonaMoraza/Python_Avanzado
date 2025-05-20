import json

##leer un json se conoce como deserializar
# Deserializar (convertir la cadena JSON a un diccionario)
with open("persona.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

# Imprimir el diccionario
print(type(datos_json))
print(datos_json)
print(datos_json["colores"])

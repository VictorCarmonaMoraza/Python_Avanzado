import json

persona = {
    "nombre": "Juan",
    "apellido": "Gomez",
    "edad": 30,
}

# Serializar (convertir el diccionario a una cadena JSON)
objeto_json = json.dumps(persona, indent=2)

# Escribir la cadena JSON a un archivo
with open("persona.json", "w") as archivo_json:
    archivo_json.write(objeto_json)


#Deserializar
with open("persona2.json", "w") as archivo2_json:
    json.dump(persona, archivo2_json)



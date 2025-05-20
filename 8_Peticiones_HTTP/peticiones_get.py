import requests
import json


response = requests.get('https://api.github.com')
#Imprimos los headers de la respuesta
#print(response.headers)

#Imprimimos el estado de la respuesta
print(response.status_code)

#Imprrimos el contenido de la respuesta
#print(response.content)
#print(response.text)
print(response.json()["current_user_url"])


print("-----------------------------------------------------")

response2 = requests.get('https://api.github.com/search/repositories',
                         params={'q':'python'},
                        )
print(response2.json())

data =response2.json()
print(data.keys())

# Guardar el objeto JSON en un archivo
objeto_json = json.dumps(data, indent=2)

with open("repositorios.json", "w") as archivo_json:
    # Escribir el objeto JSON en el archivo
    archivo_json.write(objeto_json)
    print("Archivo creado")
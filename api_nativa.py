# maneja errores al hacer solicitudes
import urllib.error
# permite hacer solicitudes http en python
import urllib.request
# maneja archivos json
import json

# endpoint de la api
api = "https://pokeapi.co/api/v2/ability/1/"
# Algunas APIs rechazan solicitudes de scripts o bots si no tienen un User-Agent válido. Los navegadores como Chrome o Firefox siempre envían este encabezado al hacer una petición. Aquí estamos simulando que la solicitud proviene de un navegador.
headers = {"User-Agent": "Mozilla/5.0"}

try:
    req = urllib.request.Request(api, headers=headers)
    response = urllib.request.urlopen(req)

    # ve a la url y guarda la respuesta
    # response = urllib.request.urlopen(api)

    # lee la respuesta y la guarda en una variable
    # los datos estan en binario, por lo que se debe decodificar
    data = response.read()

    # decodifica los datos y los guarda en una variable
    # los datos son en formato json, por lo que se debe decodificar
    json_data = json.loads(data.decode('utf-8'))

    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print("Error al conectarse a la API" + str (e))
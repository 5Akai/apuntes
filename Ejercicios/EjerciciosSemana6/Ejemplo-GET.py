import requests, pprint

#IP suministrada por el usuario
ip = input("Introducir dirección de red pública: ")

#Formato de respuesta suministrado por el usuario

responsetype = input("Formato de respuesta JSON o XML: ")

#Endpoint del servicio de APIREST

endpoint = f"http://ip-api.com/{responsetype.lower()}/{ip}"


print(f"")
print(f"Utilizamos la función GET para llamar al microservicio...")
print(f"")
print(f"")



try:
    response = requests.get(endpoint)


    if(response.status_code == 200):

        print(f"Cabeceras: {response.headers}")
        print(f"Content-Type: {response.headers['Content-Type']}")
        print(f"Content-Type Indica el formato de la información enviada en el BODY.\n")
        print(f"Content-Length: {response.headers['Content-Length']} Bytes.")
        print("Content-Length indica el tamaño en byteees de la información enviada en el BODY\n")

        #Mostramos el contenido delee mensaje de respuesta
        print(f"Contenido: {response.content}\n")
        print(f"Contenido: {response.text}\n")
        print("==============================================")

        if("application/json" in response.headers["Content-Type"].lower()):
            data= response.json()           # La función JSON retorna un objeto de tipo diccionario
            print(f"Ubicación: {data['regionName']} ({data['Country']})")
            print(f"Latitud: {data['lat']}")
            print(f"Longitud: {data['lon']}")
            print(f"Organización Proveedora de Internet: {data['isp']} - {data['org']}")
            

    else:
        print("No se puede procesar la consulta.")
    



    print(f"· Estado: {response.status_code} / {response.reason}")
    print(f"")
except requests.ConnectionError as err: #Indica errores de DNS
    print(f"{err}")
except requests.Timeout as err: #Timeout Superado
    print(f"{err}")
except requests.TooManyRedirects as err: #Demasiados redireccionamientos
    print(f"{err}")
except requests.HTTPError as err: #Indica errores HTTP
    print(f"{err}")
except requests.RequestException as err: #Genérico de requeests
    print(f"{err}")
except Exception as err: 
    print(f"{err}")

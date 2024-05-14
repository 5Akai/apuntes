import requests, pprint

#IP suministrada por el usuario
zip = input("Introducir código postal: ")

#Endpoint del servicio de APIREST

endpoint = f"https://api.zippotam.us/es/{zip}"


print(f"")
print(f"Utilizamos la función GET para llamar al microservicio...")
print(f"")
print(f"")



try:
    response = requests.get(endpoint)


    if(response.status_code == 200):

        print(f"{response})
        print("==============================================")

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
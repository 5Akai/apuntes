import requests, pprint

#IP suministrada por el usuario
zip = input("Introducir código postal: ")

#Endpoint del servicio de APIREST

endpoint = f"https://api.zippotam.us/es/{zip}"

response = requests.get(endpoint)


print(f"")
print(f"Utilizamos la función GET para llamar al microservicio...")
print(f"")
print(f"")

if(response.status_code == 200):

    print(f"{response.headers[zip]})
    print(f"Contenido: {response.content}")

print("==============================================")

else:
    print(f"No se puede procesar la consulta.")
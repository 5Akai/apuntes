import requests


# Código postal suministrado por el usuario

zip_code = input("Introducir código postal: ")


# Endpoint del servicio de API REST

endpoint = f"api.zippotam.us/es/{zip_code}"


try:

    print("Utilizamos la función GET para llamar al microservicio...")

    response = requests.get(endpoint)


    if response.status_code == 200:

        print("==")

        print(response.json())  # Utiliza .json() para obtener el contenido JSON de la respuesta

    else:

        print("No se puede procesar la consulta.")

        print(f"· Estado: {response.status_code} / {response.reason}")


except requests.ConnectionError as err:  # Indica errores de conexión

    print(f"{err}")


except requests.Timeout as err:  # Timeout superado

    print(f"{err}")


except requests.TooManyRedirects as err:  # Demasiados redireccionamientos

    print(f"{err}")


except requests.HTTPError as err:  # Errores HTTP

    print(f"{err}")


except requests.RequestException as err:  # Genérico de requests

    print(f"{err}")


except Exception as err:

    print(f"{err}")
    print(f"api.zippopotam.us/es{zip_code}")

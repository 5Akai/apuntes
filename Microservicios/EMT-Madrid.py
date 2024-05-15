## Consultar tiempo de llegada del autobus

import requests, pprint, json, os

def InfoBus(item):
    data = {}
    data["linea"] = item["line"]
    data["distancia"] = item["DistanceBus"]

    if (item["estimateArrive"] < 60):
        data["tiempo"] = "está en la parada."
    else:
        time = item["estimateArrive"] / 60
        if(time >= 20):
            data["tiempo"] = "Llegará en 20 minutos o más"
        else:
            data["tiempo"] = f"Llegará aproximadamente en {time:1.0f} minutos.."

    data["mensaje"] = f"el {data["linea"]} llegará en {data["tiempo"]}. {data["distancia"]} metros. "

    return(data)



#Obtener token de acceso al API

urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "timeArrivalBus": "transport/busemtmad/stops/<stopId>/arrives/"
}

token = ""
parada = input("Número de la parada: ")


#Obtener token de acceso al API
##try:
endpoint = urls["base"] + urls["login"]


headers = {
    "X-ClientId": "25d3d248-fc0c-479d-8276-78ac52c647f2",
    "passKey":"141FE2B578702B63F6EE4E03049F95AB594A28BA9B67A7CAFF0D08BDB8B045463A14B6EADF5885D589B00DA11919CB9D12FFC012A317404D1EF97656E67A86B0"
}

response = requests.get(endpoint, headers=headers)
if(response.status_code == 200):
    token = response.json()["data"][0]["accessToken"]
    print(token)
else:
    print(f"Error: ({response.status_code}): {response.reason}")
    quit()

endpoint2 = urls["base"] + urls["timeArrivalBus"].replace("<stopId>", parada)
headers2 = {"accessToken": token}
data2 = {

    "cultureInfo": "ES",

    "Text_StopRequired_YN": "Y",

    "Text_EstimationsRequired_YN": "Y",

    "Text_IncidencesRequired_YN": "N",

    "DateTime_Referenced_Incidencies_YYYYMMDD": "20240514"

}

response2 = requests.post(endpoint2, headers=headers2, json=data2)
#OTRA OPCIÓN#response2 = requests.post(endpoint2, headers=headers2, data=json.dumps(data2))

if (response2.status_code == 200):

    for item in response2.json()["data"][0]["Arrive"]:
        print(InfoBus(item)["mensaje"])

else:
    print(f"Error: ({response2.status_code}): {response2.reason}")






##except Exception as e:
    print(f"Error: {e}")

input("presione cualquier tecla para salir: ")
os.system('clear')
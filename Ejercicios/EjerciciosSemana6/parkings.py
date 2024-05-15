
import requests, pprint, json, os


def InfoPark(item):
    data = {}
    data["nombre"] = item["name"]
    data["calle"] = item["address"]
    data["estaLibre"] = ""
    if item["freeParking"] == None: data["estaLibre"] = "Ocupado"
    else: data["estaLibre"] = f"Libre, {item["freeParking"]} plazas libres."

    data["mensaje"] = f"[Nommbre]: {data['nombre']}\n·{data['estaLibre']}\n\n"   



    return(data)



urls = {
 
   "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "Parking": "citymad/places/parkings/availability/"
}


token = ""

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


endpoint2 = urls["base"] + urls["Parking"]
headers2 = {"accessToken": token}

data2 = {

    "cultureInfo": "ES",

    "Text_StopRequired_YN": "Y",

    "Text_EstimationsRequired_YN": "Y",

    "Text_IncidencesRequired_YN": "N",

    "DateTime_Referenced_Incidencies_YYYYMMDD": "20240514"

}


response2 = requests.get(endpoint2, headers=headers2, json=data2)

if (response2.status_code == 200):

    total = 0

    for item in response2.json()["data"]:

        
        temp = InfoPark(item)
        print(temp["mensaje"])
        if temp["estaLibre"] != None:
            total = total + 1


        
    print(f"Total de parkings libres: {total}")
else:
    print(f"Error: ({response2.status_code}): {response2.reason}")



##except Exception as e:
#    print(f"Error: {e}")

input("presione cualquier tecla para salir: ")
os.system('clear')
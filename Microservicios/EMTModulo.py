import requests, pprint, json, os

urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "timeArrivalBus": "transport/busemtmad/stops/<stopId>/arrives/"
}


token = None

def GetToken():
    endpoint = urls["base"] + urls["login"]


    headers = {
        "X-ClientId": "25d3d248-fc0c-479d-8276-78ac52c647f2",
        "passKey":"141FE2B578702B63F6EE4E03049F95AB594A28BA9B67A7CAFF0D08BDB8B045463A14B6EADF5885D589B00DA11919CB9D12FFC012A317404D1EF97656E67A86B0"
    }

    response = requests.get(endpoint, headers=headers)
    if(response.status_code == 200):
        return response.json()["data"][0]["accessToken"]
        
    else:
        return None
    
def GetArrivalBus():

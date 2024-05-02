import requests
import datetime


USERNAME = "rafaelleone"
TOKEN = "hf948923hr94w30gf0e00wa8"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "videogames",
    "name": "Gaming Time",
    "unit": "hour",
    "type": "float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

GRAPH_ID = "videogames"

videogames_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = str(datetime.datetime.today().strftime("%Y%m%d"))
x = str(input("How many hours have you played today? "))

json = {
    "date": today,
    "quantity": x
}

response = requests.post(url=videogames_endpoint, json=json, headers=headers)
print(response.text)

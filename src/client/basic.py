import requests

username = "hadi"
password = "hadi"

#Le premier endpoint permettait d'obtenir un token
#endpoint = "http://127.0.0.1:8000/user/token"
endpoint  = "http://127.0.0.1:8000/user/token"

response = requests.post(endpoint,json={'username':username,'password':password})
last = response
response = response.json()
print("************************************************************************************")
print("                                        Le Refresh                                 ")
print(response['refresh'])
print("************************************************************************************")
print("                                        Le access                                 ")
print(response['access'])
print("************************************************************************************")

print(last.status_code)
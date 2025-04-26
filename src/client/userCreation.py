import requests

endpoint = "http://127.0.0.1:8000/user/create"

data = {
    'username':'Gadjigo',
    'first_name':'Hamidou',
    'last_name':'Gadjigo',
    'date_of_birth':"2025-04-09",
    'address':'matam',
    'profile_picture':None,
    'role':'professor',
    'email':'oups379@gmail.com',
}

response = requests.post(endpoint,json=data)
if response.status_code == "200":
    print("Enregistrement effectué avec succès ")
else:
    print(response.json())
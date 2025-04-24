import requests

endpoint = "http://127.0.0.1:8000/user/create"

data = {
    'username':'adou',
    'first_name':'Mamassa',
    'last_name':'Diallo',
    'date_of_birth':"2025-04-09",
    'address':'matam',
    'profile_picture':None,
    'role':'professor'
}

response = requests.post(endpoint,json=data)
if response.status_code == "200":
    print("Enregistrement effectué avec succès ")
else:
    print(response.json())
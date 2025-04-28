import requests

endpoint = "http://127.0.0.1:8000/manager/update/1"

data = {
    'user':{
        'username':'Bordelo',
        'first_name':'Hamidou',
        'last_name':'Gadjigo',
        'date_of_birth':"2025-04-09",
        'address':'matam',
        'profile_picture':None,
        'email':'bordel@gmail.com'
    },
    "phone_nuber": "+224620260242",
    'poste':"Dirlo"
    
}

response = requests.put(endpoint,json=data)
if response.status_code == 200:
    print("Enregistrement effectué avec succès ")
else:
    print(response.json())
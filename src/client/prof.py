import requests

endpoint = "http://127.0.0.1:8000/professor/create"

data = {
    'user':{
        'username':'Gadjigoss',
        'first_name':'Hamidou',
        'last_name':'Gadjigo',
        'date_of_birth':"2025-04-09",
        'address':'matam',
        'profile_picture':None,
        'email':'hadi@gmail.com'
    },
    "phone_nuber": "+224620260243"
    
}

response = requests.post(endpoint,json=data)
if response.status_code == "200":
    print("Enregistrement effectué avec succès ")
else:
    print(response.json())
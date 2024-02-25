from requests.auth import HTTPBasicAuth
import requests
import json

token = requests.get('http://localhost:5000/login',auth=('Gabriel','123456')).json()['token']
print(token,f'\n')
data = requests.get('http://localhost:5000/autores/',headers={'x-access-token':token}).json()
print(data)
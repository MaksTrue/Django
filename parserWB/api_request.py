import requests
import pprint


token = '70517542b50898e1015ace1088e5bb700c7ce367'

headers = {'Authorization': f'Token {token}'}

response = requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers)

pprint.pprint(response.json())
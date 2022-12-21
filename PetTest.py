import requests
import json
info ={
      "id": 0,
      "category": {"id": 0, "name": "string"},
      "name": "doggie",
      "photoUrls": ["string"],
      "tags": [{"id": 0, "name": "string"}], "status": "available"}
def get():
    res = requests.get(f'https://petstore.swagger.io/v2/swagger.json', headers = {'accept': 'application/json'})
    print(res.status_code)
    print(res.json())
def post():
    res = requests.post(f'https://petstore.swagger.io/v2/pet',
                        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                        data=json.dumps(info, ensure_ascii=False))
    print(res.status_code)
    print(res.text)
def delete():
    res = requests.delete(f'https://petstore.swagger.io/v2/pet/0', headers={'accept': 'application/json'})

def put():
    res = requests.put(f'https://petstore.swagger.io/v2/pet',
                        headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                        data=json.dumps(info, ensure_ascii=False))
    print(res.status_code)
    print(res.text)


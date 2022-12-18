import json
import requests
class Pet:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"
    def api(self, email: str, passwd: str) -> json:
        headers = {'email': email, 'password': passwd}
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def get_list(self, auth_key: json, filter: str = "") -> json:
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def add(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        data = MultipartEncoder(fields={'name': name, 'animal_type': animal_type, 'age': age, 'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')})
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result
    def delete(self, auth_key: json, pet_id: str) -> json:
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def update(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: int) -> json:
        headers = {'auth_key': auth_key['key']}
        data = {'name': name, 'age': age, 'animal_type': animal_type}
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
from .base_api import BaseApi
import json
import requests


class AuthApi(BaseApi):

    def register(self, email, password) -> json:
        data = {"email": f'{email}@gmail.com',
                "password": password,
                "confirm_password": password
                }
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = res.status_code
        return status, res.json()

    def login(self, email, password) -> json:
        data = {'email': email, 'password': password}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        status = res.status_code
        return status, res.json()

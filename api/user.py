from .base_api import BaseApi
import json
import requests


class UserApi(BaseApi):

    def delete_user(self, user_id, headers) -> json:
        res = requests.delete(self.base_url + f'users/{user_id}', headers=headers)
        status = res.status_code
        return status, res.json()

    def list_users(self, headers) -> json:
        res = requests.get(self.base_url + f'users', headers=headers)
        status = res.status_code
        return status, res.json()

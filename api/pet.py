from .base_api import BaseApi
import json
import requests


class PetApi(BaseApi):

    def create_pet(self, data, headers) -> json:
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status, res.json()

    def delete_pet(self, pet_id, headers) -> json:
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status, res.json()

    def add_pet_photo(self, pet_id, headers, files) -> json:
        """Запрос к Swagger сайта для добавления фото питомца зарегистрированного пользователя """
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        return status, res.json()
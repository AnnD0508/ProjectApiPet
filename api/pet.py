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

    def get_info_about_pet(self, pet_id) -> json:
        """Запрос к Swagger сайта для получения информации о питомце"""
        res = requests.get(self.base_url + f'pet/{pet_id}')
        status = res.status_code
        return status, res.json()

    def changing_pet_details(self, pet_id, headers, data) -> json:
        """Запрос к Swagger сайта для изменения питомца"""
        res = requests.patch(self.base_url + f'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status, res.json()

    def post_pets_list(self, headers, data) -> json:
        """Запрос к Swagger сайта для получения списка питомцев"""
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status, res.json()



import json
import requests
import settings
from settings import VALID_EMAIL, VALID_PASSWORD, BASE_URL
import uuid
import os


class Pets:
    """API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self) -> json:
        # self.my_token = None
        self.base_url = settings.BASE_URL

    def register_new_user(self) -> json:
        """Запрос к Swagger сайта для получения id пользователя при регистрации """
        email = uuid.uuid4().hex
        data = {"email": f'{email}@gmail.com',
            "password": '1234',
            "confirm_password": '1234'
         }
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        user_id = res.json().get('id')
        user_token = res.json()['token']
        headers = {'Authorization': f'Bearer {user_token}'}
        params = {'id':{user_id}}
        res = requests.delete(self.base_url + f'users/{user_id }', headers=headers, params=params)
        status = res.status_code
        print(status)
        return status

    # def remove_user(self) -> json:
    #     """Запрос к Swagger сайта для удаления пользователя"""
    #     user = Pets().register_new_user()[1]
    #     id_remove_user = user.get ('id')
    #     token_remove_user = user.get ('token')
    #     headers = {'Authorization': f'Bearer {token_remove_user}'}
    #     res = requests.delete(self.base_url + f'users/{id_remove_user}',headers=headers)
    #     status = res.status_code
    #     print(status)
    #     return status

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {'email': settings.VALID_EMAIL, 'password': settings.VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, my_id, status
    # #
    # def get_list_users(self):
    #     """Запрос к Swagger сайта для получения списка пользователей"""
    #     my_token = Pets().get_token()[0]
    #     headers = {'Authorization': f'Bearer {my_token}'}
    #     res = requests.get(self.base_url + f'users', headers=headers)
    #     status = res.status_code
    #     my_id = res.text
    #     print(res.json())
    #     return status, my_id
    #
    # def registered_user_registration(self) :
    #     """Запрос к Swagger сайта для регистрации пользователя с уже существующим ID """
    #     data = {"email": 'forexz@mail.ru',
    #             "password": '54321',
    #             "confirm_password": '54321'
    #             }
    #     res = requests.post(self.base_url + 'register', data=json.dumps(data))
    #     received_id = res.json()
    #     received_id = received_id.get('id')
    #     status = res.status_code
    #     return status, received_id
    #
    def create_new_pet_and_delete(self):
        """Запрос к Swagger сайта для добавления питомца зарегистрированного пользователя """
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": 0,
                "name": 'Bayun', "type": 'cat', "age": 199, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        new_pet_id = res.json().get('id')
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{new_pet_id}', headers=headers)
        status = res.status_code
        return status



    def get_pet_photo(self):
        """Запрос к Swagger сайта для добавления фото питомца зарегистрированного пользователя """
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_new_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        file_data = open('../images/1.jpg', 'rb')
        files = {'pic': ('1.jpg', file_data, 'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def delete_pet(self):
        """Запрос к Swagger сайта для удаления питомца зарегистрированного пользователя """
        my_token = Pets().get_token()[0]
        pet_id = Pets().create_new_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}

        status = res.status_code
        return status
    #
    #
    # def get_pet_like(self):
    #     my_token = Pets().get_token()[0]
    #     """Запрос к Swagger сайта для добавления лайков питомцу зарегистрированным пользователем """
    #     pet_id = Pets().create_new_pet()[0]
    #     headers = {'Authorization': f'Bearer {my_token}'}
    #     res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
    #     status = res.status_code
    #     return status


Pets().register_new_user()

# Pets().remove_user()
Pets().create_new_pet()

# Pets().get_pet()
# Pets().get_pet_photo()
# Pets().get_pet_like()

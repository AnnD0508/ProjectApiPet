from api.pet import PetApi
import os


class PetDataToAPI:

    def create_pet_data(self, user_id, user_token):
        data = {"id": 0,
                "name": 'Bayun', "type": 'cat', "age": 199, "owner_id": user_id}
        headers = {'Authorization': f'Bearer {user_token}'}
        [status, response] = PetApi().create_pet(data, headers)
        return status, response.get('id')

    def delete_pet_data(self, pet_id, user_token):
        headers = {'Authorization': f'Bearer {user_token}'}
        [status, response] = PetApi().delete_pet(pet_id, headers)
        return status, response

    def add_pet_photo_data(self, pet_id, user_token ):
        headers = {'Authorization': f'Bearer {user_token}'}
        path = os.getcwd() + '\\..\\images\\1.jpg'
        file_data = open(path, 'r+b')
        files = {'pic': ('1.jpg', file_data, 'image/jpg')}
        [status, response] = PetApi().add_pet_photo(pet_id, headers, files)
        return status, response

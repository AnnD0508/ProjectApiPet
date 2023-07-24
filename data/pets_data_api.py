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

    def add_pet_photo_data(self, pet_id, user_token):
        headers = {'Authorization': f'Bearer {user_token}'}
        path = os.getcwd() + '\\..\\images\\1.jpg'
        file_data = open(path, 'r+b')
        files = {'pic': ('1.jpg', file_data, 'image/jpg')}
        [status, response] = PetApi().add_pet_photo(pet_id, headers, files)
        return status, response

    def get_info_by_pet_id_data(self, pet_id):
        [status, response] = PetApi().get_info_about_pet(pet_id)
        return status, response

    def changing_pet_details_data (self, pet_id, user_token):

        data = {"id": pet_id, "name": 'Vasya', "type": 'dog', "age": 200, "gender": 'Female'}
        [status, response] = PetApi().changing_pet_details(pet_id, headers, data)
        return status, response

    def post_pets_list_data(self, user_token, user_id):
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {"user_id": user_id}
        [status, response] = PetApi().post_pets_list(headers, data)
        return status, response





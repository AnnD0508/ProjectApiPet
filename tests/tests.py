from data.user_data_api import UserDataToAPI
from data.pets_data_api import PetDataToAPI


class Tests:

    def test_create_and_delete_user(self):
        registration_status, user_id, user_token = UserDataToAPI().register_new_user_data()
        assert registration_status == 200
        delete_status, delete_response = UserDataToAPI().delete_user_data(user_id, user_token)
        assert delete_status == 200

    def test_user_login(self):
        login_status, user_id, user_token = UserDataToAPI().login_user_data()
        assert login_status == 200

    def test_create_delete_pet(self):
        login_status, user_id, user_token = UserDataToAPI().login_user_data()
        assert login_status == 200
        pet_create_status, pet_id = PetDataToAPI().create_pet_data(user_id, user_token)
        assert pet_create_status == 200
        pet_delete_status, delete_response = PetDataToAPI().delete_pet_data(pet_id, user_token)
        assert pet_delete_status == 200

    def test_add_photo_pet(self):
        login_status, user_id, user_token = UserDataToAPI().login_user_data()
        assert login_status == 200
        pet_create_status, pet_id = PetDataToAPI().create_pet_data(user_id, user_token)
        assert pet_create_status == 200
        pet_add_photo_status, post_response = PetDataToAPI().add_pet_photo_data(pet_id, user_token)
        link = post_response['link']
        assert pet_add_photo_status == 200
        assert len(link) > 0

    def test_info_about_pet(self):
        login_status, user_id, user_token = UserDataToAPI().login_user_data()
        assert login_status == 200
        pet_create_status, pet_id = PetDataToAPI().create_pet_data(user_id, user_token)
        assert pet_create_status == 200
        get_pet_status, get_pet_response = PetDataToAPI().get_info_by_pet_id_date(pet_id)
        pet = get_pet_response.get('pet')
        assert get_pet_status == 200
        assert pet_id == pet.get('id')
        assert 'Bayun' == pet.get('name')
        assert 'cat' == pet.get('type')
        assert 199 == pet.get('age')
        assert user_id == pet.get('owner_id')

    # def test_create_pet(self, write_new_pet_id):
    #     login_status, user_id, user_token = UserDataToAPI().login_user()
    #     assert login_status == 200
    #     pet_create_status, pet_id = TestPetAPI().create_pet(user_id, user_token)
    #     set_pet_id, get_pet_id = write_new_pet_id
    #     set_pet_id(pet_id)
    #     assert pet_create_status == 200
    #
    # def test_delete_pet(self, write_new_pet_id):
    #     login_status, user_id, user_token = UserDataToAPI().login_user()
    #     set_pet_id, get_pet_id = write_new_pet_id
    #     pet_delete_status, delete_response = TestPetAPI().delete_pet(get_pet_id(), user_token)
    #     assert pet_delete_status == 200


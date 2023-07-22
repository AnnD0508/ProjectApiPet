import os.path
import pytest
import requests
from api.pet import Pets
from settings import VALID_EMAIL, VALID_PASSWORD, BASE_URL

pets = Pets()

def test_get_token():
    status = pets.get_token()
    assert status[2] == 200

def test_add_new_user():
    register_user = pets.register_new_user()
    status = register_user[0]
    register_user_id = register_user[1].get ('id')
    assert status == 200
    assert register_user_id != 0

def test_remove_new_user():
    remove_user = pets.remove_user()
    status = remove_user
    assert status == 200

def test_list_users():
    [status, my_id] = pets.get_list_users()
    assert status == 200
    assert my_id

def test_negativ_registration():
    [status, received_id] = pets.registered_user_registration()
    assert received_id == None
    assert status == 400

def test_add_new_pet():
    register_pet = pets.create_new_pet()
    status = register_pet[1]
    add_pet_id = register_pet[0]
    pet_id = add_pet_id
    print(add_pet_id)
    assert status == 200
    assert add_pet_id != 0

def test_add_pet_photo():
    [status, link] = pets.get_pet_photo()
    assert status == 200
    assert link

def test_remove_pet():
    status = pets.delete_pet()
    print (status)
    assert status == 200

def test_get_pet_like():
    status = pets.get_pet_like()
    print(status)
    assert status == 200








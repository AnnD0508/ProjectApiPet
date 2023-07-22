import pytest


@pytest.fixture(scope="module")
def write_new_pet_id():
    new_pet_id = None

    def set_pet_id(val):
        nonlocal new_pet_id
        new_pet_id = val

    def get_pet_id():
        return new_pet_id

    yield set_pet_id, get_pet_id

from api.user import UserApi
from api.auth import AuthApi
from settings import VALID_EMAIL, VALID_PASSWORD, BASE_URL
import uuid


class TestUserAPI:

    def register_new_user(self):
        email = uuid.uuid4().hex
        [status, response] = AuthApi().register(email, '1234')
        return status, response.get('id'), response.get('token')

    def login_user(self):
        [status, response] = AuthApi().login(VALID_EMAIL, VALID_PASSWORD)
        return status, response.get('id'), response.get('token')

    def delete_user(self, user_id, user_token):
        headers = {'Authorization': f'Bearer {user_token}'}
        [status, response] = UserApi().delete_user(user_id, headers)
        return status, response

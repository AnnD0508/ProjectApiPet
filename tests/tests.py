from test_user import TestUserAPI
import pytest


class Tests:
    def test_create_and_delete_user(self):
        [registration_status, user_id, user_token] = TestUserAPI().register_new_user()
        print(registration_status, user_id, user_token)
        assert registration_status == 200
        [delete_status,delete_response] = TestUserAPI().delete_user(user_id, user_token)
        assert delete_status == 200

    def test_user_login(self):
        [login_status, user_id, user_token] = TestUserAPI().login_user()
        assert login_status == 200

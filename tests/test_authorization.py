import allure
from endpoints.user_auth_objects import UserAuth


class TestUserAuthentication:

    @allure.title('Проверка авторизации с валидными данными пользователя')
    def test_valid_user_login(self, auth_user_data):
        auth = UserAuth()
        login_response = auth.authenticate_user(auth_user_data)
        assert login_response.status_code == 200
        assert login_response.json()['success'] is True

    @allure.title('Проверка авторизации с неверными учетными данными')
    def test_invalid_credentials_login(self):
        auth = UserAuth()
        invalid_login_response = auth.authenticate_with_invalid_credentials()
        assert invalid_login_response.status_code == 401
        assert invalid_login_response.json()['success'] is False
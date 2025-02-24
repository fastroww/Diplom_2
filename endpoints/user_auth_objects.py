import allure
import requests
from tests.data import (API_BASE_URL, LOGIN_ENDPOINT, INVALID_CREDENTIALS, ERROR_INVALID_CREDENTIALS)


class UserAuth:
    def __init__(self):
        self.api_response = None

    @allure.step('Авторизация существующего пользователя')
    def authenticate_user(self, auth_token):
        credentials = {
            'email': auth_token['email'],
            'password': auth_token['password']
        }
        headers = {
            'Authorization': auth_token["access_token"]
        }
        self.api_response = requests.post(API_BASE_URL + LOGIN_ENDPOINT, headers=headers, json=credentials)
        return self.api_response

    @allure.step('Авторизация с неверными учетными данными')
    def authenticate_with_invalid_credentials(self):
        credentials = INVALID_CREDENTIALS
        self.api_response = requests.post(API_BASE_URL + LOGIN_ENDPOINT, json=credentials)
        return self.api_response

    @allure.step('Проверка ответа при авторизации с неверными учетными данными')
    def verify_invalid_credentials_response(self):
        response_body = self.api_response.json()
        assert response_body == ERROR_INVALID_CREDENTIALS
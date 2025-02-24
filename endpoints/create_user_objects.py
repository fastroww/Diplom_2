import allure
import requests
from tests.data import API_BASE_URL, REGISTER_ENDPOINT, EXISTING_USER_DATA, USER_DATA_WITHOUT_EMAIL, ERROR_DUPLICATE_USER, ERROR_MISSING_FIELDS


class UserRegistration:

    def __init__(self):
        self.api_response = None

    @allure.step('Регистрация уже существующего пользователя')
    def register_duplicate_user(self):
        user_data = EXISTING_USER_DATA
        self.api_response = requests.post(API_BASE_URL + REGISTER_ENDPOINT, json=user_data)
        return self.api_response

    @allure.step('Регистрация пользователя без указания email')
    def register_user_without_email(self):
        user_data = USER_DATA_WITHOUT_EMAIL
        self.api_response = requests.post(API_BASE_URL + REGISTER_ENDPOINT, json=user_data)
        return self.api_response

    @allure.step('Проверка ответа при регистрации дубликата пользователя')
    def verify_duplicate_user_response(self):
        response_body = self.api_response.json()
        assert response_body == ERROR_DUPLICATE_USER

    @allure.step('Проверка ответа при регистрации пользователя без email')
    def verify_missing_email_response(self):
        response_body = self.api_response.json()
        assert response_body == ERROR_MISSING_FIELDS
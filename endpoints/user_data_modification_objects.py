import allure
import requests
from endpoints.user_auth_objects import UserAuth
from data import API_BASE_URL, ERROR_UNAUTHORIZED, USER_UPDATE_ENDPOINT


class UserDataModification(UserAuth):

    @allure.step('Обновление данных пользователя с авторизацией')
    def modify_user_data_authenticated(self, auth_token, update_data):
        headers = {
            'Authorization': auth_token["access_token"]
        }
        self.api_response = requests.patch(API_BASE_URL + USER_UPDATE_ENDPOINT, json=update_data, headers=headers)
        return self.api_response

    @allure.step('Обновление данных пользователя без авторизации')
    def modify_user_data_unauthenticated(self, update_data):
        self.api_response = requests.patch(API_BASE_URL + USER_UPDATE_ENDPOINT, json=update_data)
        return self.api_response

    @allure.step('Проверка ответа при попытке обновления данных без авторизации')
    def verify_unauthorized_update_response(self):
        response_body = self.api_response.json()
        assert response_body == ERROR_UNAUTHORIZED
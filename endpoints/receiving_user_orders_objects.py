import allure
import requests
from endpoints.order_creation_objects import OrderCreation
from tests.data import API_BASE_URL, ORDERS_ENDPOINT


class UserOrderRetrieval(OrderCreation):

    @allure.step('Получение списка заказов пользователя с авторизацией')
    def fetch_user_orders_authenticated(self, auth_token):
        self.create_authenticated_order(auth_token)
        headers = {
            'Authorization': auth_token["access_token"]
        }
        response = requests.get(API_BASE_URL + ORDERS_ENDPOINT, headers=headers)
        return response

    @allure.step('Получение списка заказов пользователя без авторизации')
    def fetch_user_orders_unauthenticated(self):
        response = requests.get(API_BASE_URL + ORDERS_ENDPOINT)
        return response
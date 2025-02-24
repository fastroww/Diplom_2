import allure
import requests
from tests.data import API_BASE_URL, INGREDIENTS_ENDPOINT, ORDERS_ENDPOINT, INVALID_INGREDIENTS_HASH, ERROR_MISSING_INGREDIENTS


class OrderCreation:

    def __init__(self):
        self.api_response = None

    @allure.step('Получение списка идентификаторов ингредиентов')
    def fetch_ingredient_ids(self):
        self.api_response = requests.get(API_BASE_URL + INGREDIENTS_ENDPOINT)
        ingredients = self.api_response.json()['data']
        return [ingredient['_id'] for ingredient in ingredients]

    @allure.step('Создание заказа с авторизацией')
    def create_authenticated_order(self, auth_token):
        ingredient_ids = self.fetch_ingredient_ids()

        order_data = {
            "ingredients": ingredient_ids[:3]
        }
        headers = {
            'Authorization': auth_token["access_token"]
        }

        response = requests.post(API_BASE_URL + ORDERS_ENDPOINT, headers=headers, json=order_data)
        return response

    @allure.step('Создание заказа без авторизации')
    def create_unauthenticated_order(self):
        ingredient_ids = self.fetch_ingredient_ids()

        order_data = {
            "ingredients": ingredient_ids[:2]
        }
        response = requests.post(API_BASE_URL + ORDERS_ENDPOINT, json=order_data)
        return response

    @allure.step('Создание заказа без указания ингредиентов')
    def create_order_without_ingredients(self, auth_token):
        headers = {
            'Authorization': auth_token["access_token"]
        }
        self.api_response = requests.post(API_BASE_URL + ORDERS_ENDPOINT, headers=headers)
        return self.api_response

    @allure.step('Создание заказа с неверным хешем ингредиентов')
    def create_order_with_invalid_hash(self):
        order_data = INVALID_INGREDIENTS_HASH
        response = requests.post(API_BASE_URL + ORDERS_ENDPOINT, json=order_data)
        return response

    @allure.step('Проверка ответа при отсутствии ингредиентов в заказе')
    def verify_missing_ingredients_response(self):
        response_data = self.api_response.json()
        assert response_data == ERROR_MISSING_INGREDIENTS
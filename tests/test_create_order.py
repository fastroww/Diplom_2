import allure
from endpoints.order_creation_objects import OrderCreation
from endpoints.receiving_user_orders_objects import UserOrderRetrieval


class TestOrderCreationAndRetrieval:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_authenticated_order(self, auth_user_data):
        order_creation = OrderCreation()
        response = order_creation.create_authenticated_order(auth_user_data)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_unauthenticated_order(self):
        order_creation = OrderCreation()
        response = order_creation.create_unauthenticated_order()
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self, auth_user_data):
        order_creation = OrderCreation()
        response = order_creation.create_order_without_ingredients(auth_user_data)
        assert response.status_code == 400
        order_creation.verify_missing_ingredients_response()

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_hash(self):
        order_creation = OrderCreation()
        response = order_creation.create_order_with_invalid_hash()
        assert response.status_code == 500

    @allure.title('Проверка получения заказов пользователя с авторизацией')
    def test_fetch_user_orders_authenticated(self, auth_user_data):
        order_retrieval = UserOrderRetrieval()
        response = order_retrieval.fetch_user_orders_authenticated(auth_user_data)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка получения заказов пользователя без авторизации')
    def test_fetch_user_orders_unauthenticated(self):
        order_retrieval = UserOrderRetrieval()
        response = order_retrieval.fetch_user_orders_unauthenticated()
        assert response.status_code == 401
        assert response.json()['success'] is False
import pytest
import requests
from tests.data import API_BASE_URL, REGISTER_ENDPOINT, USER_DELETE_ENDPOINT
from tests.generate_user_data import generate_random_user_data


@pytest.fixture(scope="function")
def setup_user():
    """
    Фикстура для создания и удаления пользователя в тестах.
    Создает пользователя, возвращает данные и удаляет пользователя после завершения теста.
    """
    user_data = generate_random_user_data()
    create_response = requests.post(API_BASE_URL + REGISTER_ENDPOINT, json=user_data)
    yield create_response, user_data  # Возвращаем ответ и данные пользователя
    access_token = create_response.json()['accessToken']
    requests.delete(API_BASE_URL + USER_DELETE_ENDPOINT, headers={'Authorization': access_token})


@pytest.fixture(scope="function")
def auth_user_data(setup_user):
    """
    Фикстура для получения данных авторизации пользователя.
    Возвращает email, пароль и токен доступа.
    """
    create_response, user_data = setup_user
    auth_data = {
        'email': user_data['email'],
        'password': user_data['password'],
        'access_token': create_response.json()['accessToken']
    }
    yield auth_data
import random

API_BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
REGISTER_ENDPOINT = 'auth/register'
USER_ENDPOINT = 'auth/user'
LOGIN_ENDPOINT = 'auth/login'
USER_UPDATE_ENDPOINT = 'auth/user'
USER_DELETE_ENDPOINT = 'auth/user'
ORDERS_ENDPOINT = 'orders'
INGREDIENTS_ENDPOINT = 'ingredients'

ERROR_DUPLICATE_USER = {
    "success": False,
    "message": "User already exists"
}

ERROR_MISSING_FIELDS = {
    "success": False,
    "message": "Email, password and name are required fields"
}

INVALID_CREDENTIALS = {
    "email": "test",
    "password": ""
}

ERROR_INVALID_CREDENTIALS = {
    "success": False,
    "message": "email or password are incorrect"
}

ERROR_UNAUTHORIZED = {
    "success": False,
    "message": "You should be authorised"
}

ERROR_MISSING_INGREDIENTS = {
    "success": False,
    "message": "Ingredient ids must be provided"
}

INVALID_INGREDIENTS_HASH = {
    "ingredients": ["1", "2"]
}

EXISTING_USER_DATA = {
    "email": "test-data@yandex.ru",
    "password": "password",
    "name": "Username"
}

USER_DATA_WITHOUT_EMAIL = {
    "email": "",
    "password": "password",
    "name": "Username"
}

RANDOM_EMAIL = f"new-test-data-{random.randint(1, 10000)}@yandex.ru"
RANDOM_NAME = f"New-Test-User-{random.randint(1, 10000)}"
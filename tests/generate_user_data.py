import random
import string
import allure


@allure.step('Создание случайных данных для нового пользователя')
def generate_random_user_data():
    """
    Генерирует случайные данные для регистрации нового пользователя.
    Возвращает словарь с email, паролем и именем.
    """
    user_email = f"user-{random.randint(1, 10000)}@example.com"
    user_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    user_name = f"User{random.randint(1, 100)}"
    return {'email': user_email, 'password': user_password, 'name': user_name}
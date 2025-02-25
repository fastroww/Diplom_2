import allure
from endpoints.user_data_modification_objects import UserDataModification
from endpoints.create_user_objects import UserRegistration
from data import RANDOM_EMAIL, RANDOM_NAME


class TestUserRegistrationAndModification:

    @allure.title('Проверка создания уникального пользователя через фикстуру')
    def test_create_unique_user(self, setup_user):
        response, _ = setup_user
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['success'] is True

    @allure.title('Проверка создания пользователя без email')
    def test_register_user_without_email(self):
        user_registration = UserRegistration()
        response = user_registration.register_user_without_email()
        assert response.status_code == 403
        user_registration.verify_missing_email_response()

    @allure.title('Проверка создания дубликата пользователя')
    def test_register_duplicate_user(self):
        user_registration = UserRegistration()
        response = user_registration.register_duplicate_user()
        assert response.status_code == 403
        user_registration.verify_duplicate_user_response()

    @allure.title('Проверка изменения email пользователя с авторизацией')
    def test_modify_user_email_authenticated(self, auth_user_data):
        update_data = {'email': RANDOM_EMAIL}
        user_modification = UserDataModification()
        response = user_modification.modify_user_data_authenticated(auth_user_data, update_data)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка изменения email пользователя без авторизации')
    def test_modify_user_email_unauthenticated(self):
        update_data = {'email': RANDOM_EMAIL}
        user_modification = UserDataModification()
        response = user_modification.modify_user_data_unauthenticated(update_data)
        assert response.status_code == 401
        assert response.json()['success'] is False

    @allure.title('Проверка изменения имени пользователя с авторизацией')
    def test_modify_user_name_authenticated(self, auth_user_data):
        update_data = {'name': RANDOM_NAME}
        user_modification = UserDataModification()
        response = user_modification.modify_user_data_authenticated(auth_user_data, update_data)
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка изменения имени пользователя без авторизации')
    def test_modify_user_name_unauthenticated(self):
        update_data = {'name': RANDOM_NAME}
        user_modification = UserDataModification()
        response = user_modification.modify_user_data_unauthenticated(update_data)
        assert response.status_code == 401
        assert response.json()['success'] is False
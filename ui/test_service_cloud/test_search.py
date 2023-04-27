import allure
from allure_commons.types import Severity
import time
from ui.model import app
from ui.model.data import fake_login, fake_password, email_random, text_random, comment


@allure.description('Scloud UI tests')
@allure.tag('UI', 'WEB')
@allure.label('owner', 'szaycev')
@allure.feature('UI')
@allure.story('Search')
class TestsSearch:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка работы поиска на главной странице')
    def test_search(self):
        # GIVEN
        browser = self

        # WHEN
        with allure.step("Открытие главной страницы"):
            app.given_scloud_opened()

        with allure.step("Ввод текста"):
            app.main.fill_input('Салон красоты')
        # THEN
        with allure.step("Поиск текста"):
            app.main.check_query_results('Салон красоты')


@allure.description('Scloud UI tests')
@allure.tag('UI', 'WEB')
@allure.label('owner', 'szaycev')
@allure.feature('UI')
@allure.story('Services')
class TestsCheckServices:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка выбора услуги ')
    def tests_check_services(self):
        # GIVEN
        browser = self

        # WHEN
        with allure.step("Открытие главной страницы"):
            app.given_scloud_opened()

        with allure.step("Выбор услуги 1С:Фреш"):
            app.main.click_to_service_fresh()

        with allure.step("Проверка результата на странице"):
            app.fresh.check_results_on_page('Фреш')


@allure.description('Scloud UI tests')
@allure.tag('UI', 'WEB')
@allure.label('owner', 'szaycev')
@allure.feature('UI')
@allure.story('Authorization')
class TestsAuthorization:
    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка авторизации с невалидными данными')
    def tests_forms_auth_is_fail(self):
        # GIVEN
        browser = self

        # WHEN
        with allure.step("Открытие главной страницы"):
            app.given_scloud_opened()

        with allure.step("Переход на форму с авторизацией"):
            app.auth.click_to_sing_in()

        with allure.step("Ввод логина"):
            app.auth.fill_login_input(fake_login)

        with allure.step("Ввод пароля"):
            app.auth.fill_password_input(fake_password)

        with allure.step("Клик на кнопку входа в аккаунт"):
            app.auth.click_submit()

        with allure.step("Проверка текста ошибки"):
            app.auth.check_error_message('Неверно указана пара логин/пароль')

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка авторизации без пароля')
    def tests_forms_auth_without_pass(self):
        # GIVEN
        browser = self

        # WHEN
        with allure.step("Открытие главной страницы"):
            app.given_scloud_opened()

        with allure.step("Переход на форму с авторизацией"):
            app.auth.click_to_sing_in()

        with allure.step("Ввод логина"):
            app.auth.fill_login_input(fake_login)

        with allure.step("Клик на кнопку входа в аккаунт"):
            app.auth.click_submit()

        with allure.step("Проверка текста ошибки"):
            app.auth.check_error_message('Для входа в личный кабинет укажите, пожалуйста, логин/пароль')

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка авторизации с невалидными данными')
    def tests_check_forgot_password_form(self):
        # GIVEN
        browser = self

        # WHEN
        with allure.step("Открытие главной страницы"):
            app.given_scloud_opened()

        with allure.step("Переход на форму с авторизацией"):
            app.auth.click_to_sing_in()

        with allure.step("Открытие формы восстановления пароля"):
            app.forgottenPasswordPage.click_forgot_your_password()

        with allure.step("Ввод логина"):
            app.forgottenPasswordPage.fill_email_input(fake_login)

        time.sleep(3)
        with allure.step("Клик на кнопку входа в аккаунт"):
            app.forgottenPasswordPage.click_submit_forgot_pass()

        with allure.step("Проверка текста ошибки"):
            app.auth.check_error_message('Логин основного пользователя не найден.')

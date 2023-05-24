import allure
from allure_commons.types import Severity
from ui.model import app


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

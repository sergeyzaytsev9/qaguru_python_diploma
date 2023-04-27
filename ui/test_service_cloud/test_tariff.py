import time
import allure
from allure_commons.types import Severity
from ui.model import app
from ui.model.data import fresh_tariff


@allure.description('Scloud UI tests')
@allure.tag('UI', 'WEB')
@allure.label('owner', 'szaycev')
@allure.feature('UI')
@allure.story('Plans')
class TestsTariff:

    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка страницы с тарифами ')
    def test_check_tariff(browser_management):

        with allure.step("Открытие главной страницы"):
            app.given_scloud_opened()

        with allure.step("Переход к странице с тарифами"):
            app.main.click_to_plans()

        with allure.step("Проверка результата на странице"):
            app.tariff.check_results_on_page("Тарифы")


    @allure.severity(Severity.NORMAL)
    @allure.title('Проверка калькулятора тарифа')
    def test_calculator_tariff(browser_management):
        with allure.step("Открытие главной страницы"):
            app.given_scloud_opened()
        with allure.step("Переход к странице с тарифами"):
            app.main.click_to_plans()
        with allure.step("Заполнение полей калькулятора"):
            app.tariff.fill_calc_form(fresh_tariff)
        with allure.step("Проверка подсчета сессий и инфобаз"):
            app.tariff.check_results_calculation(fresh_tariff)
from allure_commons._allure import step
from selene.support.shared import browser

from ui.model.components.authorization import Authorization
from ui.model.data import Service
from ui.model.pages.tariff_page import TariffPage
from ui.model.pages.main_page import MainPage
from ui.model.pages.forgotten_password_page import ForgottenPasswordPage
from ui.model.pages.fresh_page import FreshPage

main = MainPage()
fresh = FreshPage()
auth = Authorization()
tariff = TariffPage(service=Service)
forgottenPasswordPage = ForgottenPasswordPage()


@step
def given_scloud_opened():
    url = 'https://scloud.ru/'
    browser.open(url)

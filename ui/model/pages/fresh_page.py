from allure_commons._allure import step
from selene import by, have
from selene.support.shared import browser


class FreshPage:

    @step
    def check_results_on_page(self, value):
        browser.element('h1').should(have.text(value))
        return self

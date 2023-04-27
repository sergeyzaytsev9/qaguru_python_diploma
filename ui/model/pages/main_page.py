from allure_commons._allure import step
from selene import by, have,be
from selene.support.shared import browser


class MainPage:

    @step
    def fill_input(self, value):
        browser.element(by.css('#search_1')).type(value).press_enter()
        return self

    @step
    def check_query_results(self, value):
        title = browser.element('.b-serp-item:nth-child(2) .b-serp-item__title-link')
        title.should(be.visible)
        title.should(have.text(value))
        return self

    @step
    def click_to_service_fresh(self):
        browser.element('.v-dropdown__dropdownItem').click()
        browser.element('.v-dropdownInner__item.long:nth-child(2)').click()
        return self

    @step
    def click_to_plans(self):
        browser.element('.v-header__linkNavigation').element(' a[href="/tarify/"').click()
        return self

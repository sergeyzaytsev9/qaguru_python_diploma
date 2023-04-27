from allure_commons._allure import step
from selene import by, have,be
from selene.support.shared import browser


class ForgottenPasswordPage:

    @step
    def click_forgot_your_password(self):
        browser.element('.control__forgottenPassword').click()
        return self

    @step
    def fill_email_input(self, value):
        browser.element('.forgotPassword__form').element('.baseInput__entryField').type(value)
        return self

    @step
    def click_submit_forgot_pass(self):
        browser.element('.forgotPassword__buttonsWrap .forgotPassword__recovery').should(be.enabled).click()
        return self
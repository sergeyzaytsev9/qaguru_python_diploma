from selene import have
from selene.support import by
from selene.support.shared import browser
from allure_commons._allure import step


class Authorization:
    @step
    def click_to_sing_in(self):
        browser.element('.v-btnIcoAndText__text').click()
        return self

    @step
    def fill_login_input(self, value):
        browser.element('.form__login').element('.baseInput__entryField').type(value)
        return self

    @step
    def fill_password_input(self, value):
        browser.element('.form__password').element('.baseInput__entryField').type(value)
        return self

    @step
    def check_password_field_required(self):
        browser.element('.form__password').element('.input__error').should(have.text('поле является обязательным'))
        return self

    @step
    def click_submit(self):
        browser.element('.signIn__confirm').click()
        return self

    @step
    def check_error_message(self, value):
        browser.element('.popupTemplate__component').element('.popup__text').should(have.text(value))
        return self
from allure_commons._allure import step
from selene import by, have
from selene.support.shared import browser
from ui.model.components.radiobutton import Radio
from ui.model.components.checkbox import Checkbox
from ui.model.data import Service


class TariffPage:

    def __init__(self, service):
        self.service = service

    @step
    def check_results_on_page(self, value):
        browser.element('h1').should(have.text(value))
        return self

    @step
    def set_service(self, value):
        service = Radio(element=browser.element('.v-сombinedCalculator__selectedService'))
        service.set_value(value.service_name)
        return self

    @step
    def add_configurations(self):
        browser.element('.v-сombinedCalculator__parametersContainer')\
            .element('.v-сombinedCalculator__buttonPopupAddProduct')\
            .click()

    @step
    def set_configurations(self, value):
        select_configuration = Checkbox(browser.all('[for^="elem"]'))
        select_configuration.set_checkboxes(value.configuration_names)
        return self

    @step
    def submit_configurations(self):
        browser.element('.v-popupConfiguratorProductSelector') \
            .element('.v-btn__text') \
            .click()
        return self

    @step
    def check_list_configurations(self, value):
        browser.all('.v-сombinedCalculator__selectedProductsList .v-сombinedCalculator__selectedProductTitle')\
            .should(have.texts(value.configuration_names))
        return self

    @step
    def delete_configurations_on_list(self):
        browser.element('.v-buttons__wrap .v-сombinedCalculator__selectedProductDeleteButton').click()
        return self

    @step
    def add_sessions(self, value):
        sessions_container = browser.element('.v-сombinedCalculator__parametersContainerItem_usersAmmount')
        plus_button = sessions_container.element('.svg-plus-circle')
        for i in range(value.count_sessions):
            plus_button.click()

    @step
    def add_infobases(self, value):
        infobases_container = browser.element('.v-сombinedCalculator__parametersContainerItem_informationBases')
        plus_button = infobases_container.element('.svg-plus-circle')
        for i in range(value.count_infobases):
            plus_button.click()

    def check_cnt_sesions(self,value):
        browser.element('.v-сombinedCalculator__parametersContainerItem_usersAmmount')\
            .element('.v-сombinedCalculator__parameterControlsWrapper') \
            .should(have.text(str(value.summary_count_sessions)))

    def check_cnt_infobase(self, value):
        browser.element('.v-сombinedCalculator__parametersContainerItem_informationBases')\
            .element('.v-сombinedCalculator__parameterControlsWrapper')\
            .should(have.text(str(value.summary_count_infobases)))

    def fill_calc_form(self, value):
        self.set_service(value),
        self.delete_configurations_on_list(),
        self.add_configurations(),
        self.set_configurations(value),
        self.submit_configurations(),
        self.add_sessions(value),
        self.add_infobases(value)
        return self

    def check_results_calculation(self, value):
        self.check_list_configurations(value),
        self.check_cnt_sesions(value),
        self.check_cnt_infobase(value)

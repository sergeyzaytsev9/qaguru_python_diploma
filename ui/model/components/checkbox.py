from selene import have


class Checkbox:
    def __init__(self, element):
        self.element = element

    def set_checkboxes(self, list_value):
        for value in list_value:
            self.element.element_by(have.text(value)).click()

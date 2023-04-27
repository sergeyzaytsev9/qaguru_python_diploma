from selene import have
from selene.support import by
from selene.support.shared import browser


class Radio:

    def __init__(self, element):
        self.element = element

    def set_value(self, value):
        self.element.element('label[for*="'+value+'"]').click()

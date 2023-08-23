
from .main_page import MainPage

from ConfigurationFiles.library_locators import LibraryPageLoc


class LibraryClass(MainPage):
    """
    Основные действия в модуле библиотека

    """

    def open_library(self):
        """
        Открыть библиотеку
        """

        self.log_in()
        return self.go_to_library()

    # clicks
    def click_on_vendor_button(self):
        """Нажать на кнопку вендора/имя юзера"""

        button = self.find_element(LibraryPageLoc.VENDOR_BUTTON_LOCATOR)
        return self.click_button(button)

    def click_plus_button(self):
        """Кликнуть на довабление структуры"""

        button = self.find_element(LibraryPageLoc.ADD_STRUCTURE_BUTTON)
        return self.click_button(button)

    def click_aroow_structure_lvl1(self):
        return self.find_element(LibraryPageLoc.FiRST_STRUCTURE_ARROW_NAME).click()

    def click_create_button(self):
        """Кликнуть Создать"""
        button = self.find_element(LibraryPageLoc.PLUS_STRUCTURE_LVL0)
        return self.click_button(button)

    def click_add_product(self):
        return self.find_element(LibraryPageLoc.ADD_PRODUCT_BUTTON).click()

    # Adds

    def add_structure(self, name):
        """Добавление структуры"""

        field = self.find_element(LibraryPageLoc.STRUCTURE_NAME_FIELD)
        self.tipe_to_field(text=name, element=field)
        return self.click_create_button()

    def add_product(self):
        name_field = self.find_element(LibraryPageLoc.PR_NAME_FIELD)
        self.tipe_to_field(element=name_field, text="Продукт1")
        short_name_field = self.find_element(LibraryPageLoc.PR_SHORT_NAME)
        self.tipe_to_field(element=short_name_field, text="Product1")
        mera_field = self.find_element(LibraryPageLoc.PR_MERA)
        self.tipe_to_field(element=mera_field, text="Product1")
        contety_field = self.find_element(LibraryPageLoc.PR_CONTETY)
        return self.tipe_to_field(element=contety_field, text="Product1")

    def collect_buttons_text(self, locator):
        """ Собрать текст всех кнопок """

        return self.find_elements(locator)

    def find_vendor_name(self):
        return self.find_element(LibraryPageLoc.VENDOR_NAME).text

    def click_plus_lvl1(self):
        """Кликнуть на плюс на 1 уровне структуры"""
        return self.find_element(LibraryPageLoc.PLUS_STRUCTURE_LVL1).click()

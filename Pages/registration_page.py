from .base_page import BasePage
from ConfigurationFiles.main_config import *
from ConfigurationFiles.auth_page_loc import *


class RegisrationPage(BasePage):

    def open_registration_page(self):
        registration_page = self.go_to_page(Urls.REGISTRATION)
        return registration_page


    def type_emeil(self):
        email = self.find_element(FieldLoc.EMAIL_FIELD)
        return self.tipe_to_field(text=Credentials.EMAIL, element=email)

    def type_password(self):
        password = self.find_element(FieldLoc.PASSWORD_FIELD)
        return self.tipe_to_field(text=Credentials.PASSWORD, element=password)

    def reenter_password(self):
        password = self.find_element(FieldLoc.PASSWORD_FIELD2)
        return self.tipe_to_field(text=Credentials.PASSWORD, element=password)

    def to_click_agree_to_condinals(self):
        button = self.find_element(ButtonLoc.COMFIRM)
        return self.click_button(button)

    def subbmit_regisration(self):
        button = self.find_element(ButtonLoc.SUBMIT_REGISTRATION)
        return self.click_button(button)

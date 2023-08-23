from ConfigurationFiles import auth_page_loc
from .base_page import BasePage


class LoginCLass(BasePage):

    def enter_email(self, email):
        email_field = self.find_element(auth_page_loc.FieldLoc.EMAIL_FIELD)
        return self.tipe_to_field(text=email, element=email_field)

    def enter_password(self, password):
        pass_field = self.find_element(auth_page_loc.FieldLoc.PASSWORD_FIELD)
        return self.tipe_to_field(text=password, element=pass_field)

    def click_conform_button(self):
        button = self.find_element(auth_page_loc.ButtonLoc.SUBMIT)
        return self.click_button(button)

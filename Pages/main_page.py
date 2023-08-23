import time

from ConfigurationFiles import main_page_loc, main_config
from .login_page import LoginCLass


class MainPage(LoginCLass):

    def log_in(self):
        self.go_main_page()
        self.enter_email(main_config.Credentials.EMAIL)
        self.enter_password(main_config.Credentials.PASSWORD)
        self.click_conform_button()
        return self.find_element(main_page_loc.Headers.USER_NAME, time=20)

    def go_to_library(self):
        button = self.find_element(main_page_loc.Buttons.LIB_BUTTON, time=20)
        return self.click_button(button)

    def go_to_project(self):
        button = self.find_element(main_page_loc.Buttons.PROJECT_BUTTON)
        return self.click_button(button)

    def click_at_edit_project_button(self):
        edit = self.find_element(main_page_loc.Buttons.EDIT_PROJECT)
        return self.click_button(edit)

    def click_on_edit_project_name(self):
        edit_name = self.find_element(main_page_loc.Buttons.EDIT_PROJECT_NAME)
        return self.click_button(edit_name)

    def enter_project_name(self):
        name_field = self.find_element(main_page_loc.Field.INPUT_NAME)
        name_field.clear()
        return self.tipe_to_field(element=name_field, text="Измененное название")

    def click_conform_name_button(self):
        button = self.find_element(main_page_loc.Field.SUBMIT_NAME)
        return self.click_button(button)

    def take_value_from_project(self):
        field = self.find_element(main_page_loc.Field.INPUT_NAME)
        return field.get_attribute('value')

    def click_to_add_project_button(self):
        button = self.find_element(main_page_loc.Buttons.ADD_PROJECT)
        return self.click_button(button)

    def check_project_is_added(self):
        time_c = self.find_element(main_page_loc.Field.CREATE_TIME)
        return print(time_c.text)

    def click_on_delete_button(self):
        button = self.find_element(main_page_loc.Buttons.DELETE_BUTTONS)
        return self.click_button(button)

    def check_empty_massege(self):
        massege = self.find_element(main_page_loc.Field.EMPTY_MASEGE)
        time.sleep(2)
        print(massege.text)

        return massege.text

        # project = self.find_element(main_page_loc.Field.PROJECT)
        # if len(project):
        #     print("Project is displyed")
        #     return False
        #
        # else:
        #     print("Project not displaed")
        #     return True
        #
        #

from Pages import main_page
import time


class TestMainPage:

    def test_add_project(self, broweser):
        main = main_page.MainPage(broweser)
        main.log_in()
        main.click_to_add_project_button()
        main.check_project_is_added()

    def test_edit_progect_name(self, broweser):
        main = main_page.MainPage(broweser)
        main.log_in()
        main.click_at_edit_project_button()
        main.click_on_edit_project_name()
        main.enter_project_name()
        main.click_conform_name_button()
        assert main.take_value_from_project() == "Измененное название"

    def test_delete_project(self, broweser):
        main = main_page.MainPage(broweser)
        main.log_in()
        main.click_at_edit_project_button()
        main.click_on_delete_button()
        assert main.check_empty_massege() == 'Начните работу, создав новый проект'

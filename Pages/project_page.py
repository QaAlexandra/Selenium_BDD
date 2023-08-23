from .main_page import MainPage
from ConfigurationFiles import progect_loc
from .main_page import MainPage


class ProjectPage(MainPage):

    def open_project(self):
        self.log_in()
        return self.go_to_project()

    def go_to_3d_modul(self):
        button = self.find_element(progect_loc.ProjectButtons.MODUL_3D)
        return self.click_button(button)

    def switch_iframe_to_3d(self):
        iframe = self.find_element(progect_loc.Iframe.Modul_3d)
        return self.switch_to_iframe(iframe)

    def background_button(self):
        _ = self.find_element(progect_loc.Elements3D.BACKGROUND_3D).text
        print(_)
        return _

    def canvas_is_displaed(self):
        return self.find_element(progect_loc.Iframe.CANVAS_3D)

    def go_to_specification(self):
        spec_tab = self.find_element(progect_loc.ProjectButtons.SPECIFICATION)
        return self.click_button(spec_tab)

    def specification_is_displayed(self):
        spec_tab = self.find_element(progect_loc.ProjectButtons.SPEC_BUTTON_COLUMN)
        return spec_tab.is_enabled()

    def switch_to_drawio(self):
        drawio = self.find_element(progect_loc.Iframe.DRAWIO)
        return self.switch_to_iframe(drawio)

    def faind_drawio_element(self):
        _ = self.find_element(progect_loc.Elements2D.FIGURE_2D).text
        print(_)
        return _

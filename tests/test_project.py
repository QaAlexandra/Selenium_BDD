from Pages import project_page
from Assertions.progect_assertions import element_is_displayed

import time


class TestOpenProject:
    def test_3d_modul_is_open(self, broweser):
        """CHeck 3d editor is open 3д"""
        project = project_page.ProjectPage(broweser)
        project.open_project()
        project.go_to_3d_modul()
        project.switch_iframe_to_3d()
        project.canvas_is_displaed()
        project.background_button()
        time.sleep(15)



    def test_specification_is_open(self, broweser):
        """Check specification is displayed"""
        project = project_page.ProjectPage(broweser)
        project.open_project()
        project.go_to_specification()
        project.specification_is_displayed()

    def test_2d_module_is_displeyed(self, broweser):
        """Check 2d editor is displayed"""
        p = project_page.ProjectPage(broweser)
        p.open_project()
        p.switch_to_drawio()
        p.faind_drawio_element()

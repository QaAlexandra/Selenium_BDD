from Assertions.elements import assert_h3
from Pages import login_page, main_page, lib_page

from ConfigurationFiles.main_config import Credentials


import time


def test_login(broweser):
    l = login_page.LoginCLass(broweser)
    l.go_main_page()
    l.enter_email(Credentials.EMAIL)
    l.enter_password(Credentials.PASSWORD)
    l.click_conform_button()



def test_lib(broweser):

    l = lib_page.LibraryClass(broweser)
    l.open_library()
    l.click_on_vendor_button()
    l.click_plus_button()
    l.add_structure("Уровень 1.1")
    l.click_aroow_structure_lvl1()
    l.add_product()
    l.click_add_product()

    time.sleep(60)


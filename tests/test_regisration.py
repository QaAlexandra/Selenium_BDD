import time

from Pages import login_page, main_page, registration_page

from ConfigurationFiles.main_config import Credentials



def test_registration(broweser):

    reg = registration_page.RegisrationPage(broweser)

    reg.open_registration_page()
    reg.type_emeil()
    reg.type_password()
    reg.reenter_password()
    reg.to_click_agree_to_condinals()
    reg.subbmit_regisration()
    time.sleep(20)




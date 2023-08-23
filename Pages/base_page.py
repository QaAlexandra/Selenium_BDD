from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ConfigurationFiles import main_config


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # self.driver.get(main_config.Urls.MAIN_URL)
        # self.driver.maximize_window()

    def go_main_page(self):
        self.driver.get(main_config.Urls.MAIN_URL)
        self.driver.maximize_window()

    # Найти элемент
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # Найти элементы
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    # Написать в поле
    def tipe_to_field(self, text, element):
        return element.send_keys(text)

    @staticmethod
    def click_button(element):
        return element.click()

    def go_to_page(self, url):
        self.driver.get(url)
        return self.driver.maximize_window()

    def switch_to_iframe(self, element):

        return self.driver.switch_to.frame(element)

    def set_logs(self):
        self.driver
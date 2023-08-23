import pytest

from selenium import webdriver



@pytest.fixture(scope="module")
def broweser():
    driver = webdriver.Chrome(executable_path="./sdriver/chromedriver_linux64(1)/chromedriver")
    yield driver
    driver.quit()
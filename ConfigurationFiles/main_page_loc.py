from selenium.webdriver.common.by import By


class Headers:

    USER_NAME = (By.XPATH,
                 '//*[@id="__next"]/div[1]/div[2]/main/div/div[1]/div/div/div[1]/div/div/div/h1')


class Buttons:

    LIB_BUTTON = (By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/nav/div[1]/button[3]')
    PROJECT_BUTTON = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div[4]/div/ul/li[1]/div[1]')
    EDIT_PROJECT = (By.XPATH, '//*[@id="headlessui-popover-button-:r0:"]')
    EDIT_PROJECT_NAME = (By.XPATH, '//*[@id="headlessui-popover-panel-:r1:"]/div[1]/button[1]')
    ADD_PROJECT = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div[4]/div/button')
    DELETE_BUTTONS = (By.XPATH,
                      '/html/body/div/div[1]/div[2]/main/div/div[4]/div/ul/li/div[2]/div[2]/div/div[2]/div[2]/button')
class Field:

    INPUT_NAME = (By.XPATH,
                  '//*[@id="__next"]/div[1]/div[2]/main/div/div[4]/div/ul/li[1]/div[2]/div[1]/div[1]/input')
    SUBMIT_NAME = (By.XPATH,
               '//*[@id="__next"]/div[1]/div[2]/main/div/div[4]/div/ul/li[1]/div[2]/div[1]/div[1]/div/button[1]')
    PROJECT_NAME = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div[4]/div/ul/li[1]/div[2]/div[1]/div[1]/input')
    CREATE_TIME = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div[4]/div/ul/li[1]/div[2]/div[1]/div[2]')
    PROJECT = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div[4]/div/ul/li/div[1]/div/svg')
    EMPTY_MASEGE = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div[4]/p')
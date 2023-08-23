from selenium.webdriver.common.by import By

class ProjectButtons:

    MODUL_3D = (By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[1]/div[1]/div/div[3]')
    SPECIFICATION = (By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[1]/div[1]/div/div[5]')
    SPEC_BUTTON_COLUMN = (By.XPATH, '//*[@id="headlessui-menu-button-:ru:"]')

class Iframe:

    Modul_3d = (By.XPATH, '//*[@id="__next"]/main/div/div/div[9]/div/iframe')
    DRAWIO = (By.XPATH, '//*[@id="__next"]/main/div/div/div[8]/div/iframe')

    CANVAS_3D = (By.XPATH, '//*[@id="viewport"]/canvas')

class Elements3D:

    BACKGROUND_3D = (By.XPATH, '//*[@id="scene"]/span/div[1]/div[2]/span[1]')


class Elements2D:

    FIGURE_2D = (By.XPATH, '/html/body/div[5]/div[1]/div[1]/a[2]')
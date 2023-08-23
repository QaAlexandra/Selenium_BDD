from selenium.webdriver.common.by import By


class FieldLoc:
    EMAIL_FIELD = (By.ID, "email-address")
    PASSWORD_FIELD = (By.ID, "password")
    PASSWORD_FIELD2 = (By.ID, "password2")


class ButtonLoc:
    SUBMIT = (By.XPATH, '//*[@id="__next"]/div[1]/main/div/form/div[1]/div[2]/button')
    COMFIRM = (By.ID, "confirm")
    SUBMIT_REGISTRATION = (By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div[1]/form/div/div[4]/button')

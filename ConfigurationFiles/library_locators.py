from selenium.webdriver.common.by import By


class LibraryPageLoc:
    # Structure

    STRUCTURE_NAME_FIELD = (By.NAME, 'Наименование и техническая характеристика')
    FiRST_STRUCTURE_ARROW_NAME = (By.XPATH,
                                  '//*[@id="__next"]/div[1]/div[2]/main/div/div/div[1]/div[1]/div/div['
                                  '2]/div/div/div/button')
    PLUS_STRUCTURE_LVL0 = (
        By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div/div/form/div[2]/button[2]')
    PLUS_STRUCTURE_LVL1 = (By.XPATH,
                           '//*[@id="__next"]/div[1]/div[2]/main/div/div/div[1]/div[1]/div/div['
                           '2]/div/div/div/button/div[2]/button[1]')
    FiRST_STRUCTURE_ARROW = (
        By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div/div/div/button')
    ADD_STRUCTURE_BUTTON = (
        By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div/button/div[2]/button[1]')

    # Product

    PR_NAME_FIELD = (By.NAME, "Наименование и техническая характеристика")
    PR_SHORT_NAME = (By.NAME, "Короткое название")
    PR_MERA = (By.NAME, "Единица измерения")
    PR_CONTETY = (By.ID, "Количество")

    ADD_PRODUCT_BUTTON = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div/div[1]/div[2]/div[2]/div[3]/button')

    # Buttons

    VENDOR_BUTTON_LOCATOR = (
        By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div/button')

    BUTTON_TAG = (By.TAG_NAME, "span")

    TAG_1 = (By.TAG_NAME, "h3")

    VENDOR_NAME = (By.CLASS_NAME, " ml-0")

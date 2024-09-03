from selenium.webdriver.common.by import By


class Locators:
    # login
    USERNAME_FIELD = (By.ID, 'id_username')
    PASSWORD_FIELD = (By.ID, 'id_password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'submit-row')

    # global search
    SEARCH_BAR = (By.ID, 'searchbar')
    SEARCH_BUTTON = (By.XPATH, "//input[@value='Search']")
    RESULT_LIST = (By.ID, 'result_list')

    # local results search
    PRODUCT_NAME = (By.CSS_SELECTOR, '.field-product_name')
    GUID = (By.CSS_SELECTOR, '.field-guid')
    VENDOR_CODE = (By.CSS_SELECTOR, '.field-vendor_code')
    COLOR = (By.CSS_SELECTOR, '.field-color')
    BAR_CODE = (By.CSS_SELECTOR, '.field-bar_code')
    FREQUENCY = (By.CSS_SELECTOR, '.field-frequency')
    COUNTRY = (By.CSS_SELECTOR, '.field-country')
    PRO_ACCOUNT_EMAIL = (By.CSS_SELECTOR, '.field-pro_account_email')
    PRO_ACCOUNT_NAME = (By.CSS_SELECTOR, '.field-pro_account_name')
    QR_BOX = (By.CSS_SELECTOR, '.field-qr_box')
    WHITE_LABEL = (By.CSS_SELECTOR, '.field-white_label img')
    REF = (By.CSS_SELECTOR, '.field-ref img')
    PD = (By.CSS_SELECTOR, '.field-pd img')
    DISTRIBUTION_CHANNEL = (By.CSS_SELECTOR, '.field-distribution_channel')
    STATUS = (By.CSS_SELECTOR, '.field-status')

    # filtration
    PRODUCT_NAME_DETAILS = (By.ID, 'product-name_details')
    FILTER_OPTION = lambda param: (By.XPATH, f"//option[@value='{param}']")
    APPLY_BUTTON = (By.XPATH, '//button[contains(text(), "Apply")]')
    TOTAL_RESULTS = (By.CLASS_NAME, 'small.quiet')
<<<<<<< HEAD
    CLEAR_FILTERS_LINK = (By.XPATH, '//h3[@id="changelist-filter-clear"]/a')
=======
    CLEAR_FILTERS_LINK = (By.XPATH, '//h3[@id="changelist-filter-clear"]/a')
>>>>>>> dc52b0d7051906cee607538534b1462dec5df510

import os
from typing import List, Any, Dict
from locators import Locators

def normalize_text_elements(elements) -> List[Any]:
    return [None if element.text == '-' else element.text for element in elements]


def normalize_attribute_elements(elements, attribute) -> List[Any]:
    return [1 if element.get_attribute(attribute) == 'True' else 0 for element in elements]


class BufferPage:
    URL = os.getenv('ADM_URL')


    def __init__(self, browser) -> None:
        self.driver = browser


    def login(self) -> None:
        login_elem = self.driver.find_element(*Locators.USERNAME_FIELD)
        pass_elem = self.driver.find_element(*Locators.PASSWORD_FIELD)
        login_elem.send_keys(os.getenv('ADM_USR'))
        pass_elem.send_keys(os.getenv('ADM_PWD'))
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    def search_filtered_records(self, search_param) -> Dict[str, List[Any]]:
        search_field = self.driver.find_element(*Locators.SEARCH_BAR)
        search_field.clear()
        search_field.send_keys(search_param)
        self.driver.find_element(*Locators.SEARCH_BUTTON).click()
        stats_table = self.driver.find_element(*Locators.RESULT_LIST)
        normalized_data_dict_from_admin = {
            'product_name': normalize_text_elements(
                stats_table.find_elements(*Locators.PRODUCT_NAME)
            ),
            'guid': normalize_text_elements(
                stats_table.find_elements(*Locators.GUID)
            ),
            'vendor_code': normalize_text_elements(
                stats_table.find_elements(*Locators.VENDOR_CODE)
            ),
            'color': normalize_text_elements(
                stats_table.find_elements(*Locators.COLOR)
            ),
            'bar_code': normalize_text_elements(
                stats_table.find_elements(*Locators.BAR_CODE)
            ),
            'frequency': normalize_text_elements(
                stats_table.find_elements(*Locators.FREQUENCY)
            ),
            'country': normalize_text_elements(
                stats_table.find_elements(*Locators.COUNTRY)
            ),
            'pro_account_email': normalize_text_elements(
                stats_table.find_elements(*Locators.PRO_ACCOUNT_EMAIL)
            ),
            'pro_account_name': normalize_text_elements(
                stats_table.find_elements(*Locators.PRO_ACCOUNT_NAME)
            ),
            'qr_box': normalize_text_elements(
                stats_table.find_elements(*Locators.QR_BOX)
            ),
            'white_label': normalize_attribute_elements(
                stats_table.find_elements(*Locators.WHITE_LABEL), 'alt'
            ),
            'ref': normalize_attribute_elements(
                stats_table.find_elements(*Locators.REF), 'alt'
            ),
            'pd': normalize_attribute_elements(
                stats_table.find_elements(*Locators.PD), 'alt'
            ),
            'distribution_channel': normalize_text_elements(
                stats_table.find_elements(*Locators.DISTRIBUTION_CHANNEL)
            ),
            'status': [
                element.text.lower() for element in stats_table.find_elements(*Locators.STATUS)
            ],
        }
        return normalized_data_dict_from_admin

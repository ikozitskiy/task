import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DriverSet:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def close(self):
        self.driver.close()

class BufferPage(DriverSet):
    URL = os.getenv('ADM_URL')
    def __init__(self):
        super().__init__()
    def login(self):
        self.driver.get(BufferPage.URL)
        self.driver.maximize_window()
        login_elem = self.driver.find_element(By.ID, 'id_username')
        pass_elem = self.driver.find_element(By.ID, 'id_password')
        login_elem.send_keys(os.getenv('ADM_USR'))
        pass_elem.send_keys(os.getenv('ADM_PWD'))
        btn_login_elem = self.driver.find_element(By.CLASS_NAME, 'submit-row').click()
    def search_filtered_records(self,search_param):
        search_field = self.driver.find_element(By.ID, 'searchbar')
        search_field.send_keys(search_param)
        btn_search_elem = self.driver.find_element(By.XPATH, "//input[@value='Search']").click()
        stats_table = self.driver.find_element(By.ID, 'result_list')
        product_name_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-product_name')
        guid_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-guid')
        vendor_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-vendor_code')
        color_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-color')
        barcode_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-bar_code')
        frequency_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-frequency')
        country_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-country')
        pro_acc_email_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-pro_account_email')
        pro_acc_name_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-pro_account_name')
        qr_box_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-qr_box')
        white_label_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-white_label img')
        ref_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-ref img')
        pd_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-pd img')
        distribution_channel_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-distribution_channel')
        status_elements = stats_table.find_elements(By.CSS_SELECTOR, '.field-status')
        search_field = self.driver.find_element(By.ID, 'searchbar')
        search_field.clear()
        return (product_name_elements,guid_elements,vendor_elements,color_elements,barcode_elements,frequency_elements,
                country_elements,pro_acc_email_elements,pro_acc_name_elements,qr_box_elements,white_label_elements,
                ref_elements,pd_elements,distribution_channel_elements,status_elements)

    def get_quantity_for_product(self,parameter):
        options  = self.driver.find_element(By.ID,'product-name_details').click()
        Socket_checkbox = self.driver.find_element(By.XPATH, f"//option[@value='{parameter}']").click()
        button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Apply")]')
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.execute_script("arguments[0].click();", button)
        total_results = self.driver.find_element(By.CLASS_NAME, 'small.quiet').text
        clear_filters_link = self.driver.find_element(By.XPATH, '//h3[@id="changelist-filter-clear"]/a').click()
        return int(total_results.split()[0])


    def close_drv(self):
        self.driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

    def start_browser(self, url) -> None:
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self) -> None:
        self.driver.close()

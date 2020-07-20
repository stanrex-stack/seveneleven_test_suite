from seveneleven_test_suite.pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):

    def main_open(self):
        self.open_page()


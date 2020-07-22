from pages.main_page import MainPage
from pages.main_header_page import MainPageHeader
from pages.main_page_footer import MainPageFooter


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.main_page_header = MainPageHeader(self.driver)
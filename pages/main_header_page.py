from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPageHeader(Page):
    SEVEN_ELEVEN_LOGO_LOCATOR = (By.CSS_SELECTOR, '.hdr-logo')
    SEVEN_REWARDS_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#menu-item-0 a')
    FOOD_HOVEROVER_LOCATOR = (By.CSS_SELECTOR, '#menu-item-1 a')
    BEVERAGE_HOVEROVER_LOCATOR = (By.CSS_SELECTOR, '#menu-item-2 a')
    MONEY_HOVEROVER_LOCATOR = (By.CSS_SELECTOR, '#menu-item-3 a.is-active')
    SEVEN_NOW_DELIVIRY_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#menu-item-4 a')

    FIND_A_STORE_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'ul.hdr-secondary-nav a.find-a-store')
    ACCOUNT_BUTTON_LOCATOR = (By.CSS_SELECTOR, 'ul.hdr-secondary-nav a.account')

    def verify_field_text(self, field_name, expected_text):
        if field_name == "7-Eleven":
            locator = self.SEVEN_ELEVEN_LOGO_LOCATOR
        elif field_name == "7Rewards":
            locator = self.SEVEN_REWARDS_BUTTON_LOCATOR
        elif field_name == "Food":
            locator = self.FOOD_HOVEROVER_LOCATOR
        elif field_name == "Beverages":
            locator = self.BEVERAGE_HOVEROVER_LOCATOR
        elif field_name == "Money":
            locator = self.MONEY_HOVEROVER_LOCATOR
        elif field_name == "7NOW Delivery":
            locator = self.SEVEN_NOW_DELIVIRY_BUTTON_LOCATOR
        elif field_name == "Find a Store":
            locator = self.FIND_A_STORE_BUTTON_LOCATOR
        elif field_name == "Account":
            locator = self.ACCOUNT_BUTTON_LOCATOR
        else:
            raise Exception("No such field name found")
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected: \"{expected_text}\", but got: \"{actual_text}\"'

    def verify_item_is_clickable(self, field_name):
        if field_name == "7-Eleven":
            locator = self.SEVEN_ELEVEN_LOGO_LOCATOR
        elif field_name == "7Rewards":
            locator = self.SEVEN_REWARDS_BUTTON_LOCATOR
        elif field_name == "7NOW Delivery":
            locator = self.SEVEN_NOW_DELIVIRY_BUTTON_LOCATOR
        elif field_name == "Find a Store":
            locator = self.FIND_A_STORE_BUTTON_LOCATOR
        elif field_name == "Account":
            locator = self.ACCOUNT_BUTTON_LOCATOR
        else:
            raise Exception("No such field name found")
        self.driver.wait.until(EC.element_to_be_clickable(locator))

    def hover_over_header_button(self, field_name):
        if field_name == "Food":
            locator = self.FOOD_HOVEROVER_LOCATOR
        elif field_name == "Beverages":
            locator = self.BEVERAGE_HOVEROVER_LOCATOR
        elif field_name == "Money":
            locator = self.MONEY_HOVEROVER_LOCATOR
        else:
            raise Exception("No such field name found")
        self.wait_for_element_to_be_located(*locator)
        self.hover_over_element(*locator)
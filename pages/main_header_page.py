from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPageHeader(Page):
    SEVEN_ELEVEN_LOGO_LOCATOR = (By.CSS_SELECTOR, '.hdr-logo')


    SEVEN_REWARDS_BUTTON_LOCATOR = (By.CSS_SELECTOR, '#menu-item-0 a')

    #  HOVEROVER BUNCH
    FOOD_HOVEROVER_LOCATOR = (By.CSS_SELECTOR, '#menu-item-1 a')
    BEVERAGE_HOVEROVER_LOCATOR = (By.CSS_SELECTOR, '#menu-item-2 a')
    MONEY_HOVEROVER_LOCATOR = (By.CSS_SELECTOR, '#menu-item-3 a.is-active')
    # HOVEROVER_FOOD
    FOOD_HOT_FOOD_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/hot-foods"]')
    FOOD_HEALTHY_CHOICES_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/healthy-choices"]')
    FOOD_SANDVICHES_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/sandwiches"]')
    FOOD_BAKERY_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/bakery"]')
    FOOD_BREAKFAST_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/breakfast"]')
    FOOD_PIZZA_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/pizza"]')
    FOOD_SNACKS_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/chips"]')
    FOOD_ICE_CREAM_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/ice-cream"]')
    FOOD_CANDY_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-1 a[href*="/candy"]')
    # HOVEROVER_BEVERAGERS
    BEVERAGES_COFFEE = (By.CSS_SELECTOR, 'ul#subnav-2 a[href*="/coffee"]')
    BEVERAGES_COLD_PRESSED_JUCIES = (By.CSS_SELECTOR, 'ul#subnav-2 a[href*="/cold-pressed-juices"]')
    BEVERAGES_BEER_AND_WINE = (By.CSS_SELECTOR, 'ul#subnav-2 a[href*="/beer-wine"]')
    BEVERAGES_ENERGY_SHOTS_AND_DRINKS = (By.CSS_SELECTOR, 'ul#subnav-2 a[href*="/energy-shots"]')
    BEVERAGES_BIG_GULP = (By.CSS_SELECTOR, 'ul#subnav-2 a[href*="/big-gulp"]')
    BEVERAGES_SLURPEE = (By.CSS_SELECTOR, 'ul#subnav-2 a[href*="/slurpee"]')
    # HOVEROVER_MONEY
    MONEY_GET_STIMULUS_READY_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-3 a[href*="/www.transact"]')
    MONEY_FINANCIAL_SERVICES_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-3 a[href*="/financial"]')
    MONEY_GIFT_CARDS_LOCATOR = (By.CSS_SELECTOR, 'ul#subnav-3 a[href*="/gift-cards"]')



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
        elif field_name == "Hot Foods":
            locator = self.FOOD_HOT_FOOD_LOCATOR
        elif field_name == "Healthy Choices":
            locator = self. FOOD_HEALTHY_CHOICES_LOCATOR
        elif field_name == "Sandwiches":
            locator = self.FOOD_SANDVICHES_LOCATOR
        elif field_name == "Bakery":
            locator = self.FOOD_BAKERY_LOCATOR
        elif field_name == "Breakfast":
            locator = self.FOOD_BREAKFAST_LOCATOR
        elif field_name == "Pizza":
            locator = self.FOOD_PIZZA_LOCATOR
        elif field_name == "Snacks":
            locator = self.FOOD_SNACKS_LOCATOR
        elif field_name == "Ice Cream":
            locator = self.FOOD_ICE_CREAM_LOCATOR
        elif field_name == "Candy":
            locator = self.FOOD_CANDY_LOCATOR
        elif field_name == "Coffee":
            locator = self.BEVERAGES_COFFEE
        elif field_name == "Cold Pressed Juices":
            locator = self.BEVERAGES_COLD_PRESSED_JUCIES
        elif field_name == "Beer And Wine":
            locator = self.BEVERAGES_BEER_AND_WINE
        elif field_name == "Energy Shots And Drinks":
            locator = self.BEVERAGES_ENERGY_SHOTS_AND_DRINKS
        elif field_name == "Big Gulp":
            locator = self.BEVERAGES_BIG_GULP
        elif field_name == "Slurpee":
            locator = self.BEVERAGES_SLURPEE
        elif field_name == "Get Stimulus Ready":
            locator = self.MONEY_GET_STIMULUS_READY_LOCATOR
        elif field_name == "Financial Services":
            locator = self.MONEY_FINANCIAL_SERVICES_LOCATOR
        elif field_name == "Gift Cards":
            locator = self.MONEY_GIFT_CARDS_LOCATOR
        else:
            raise Exception("No such field name found")
        self.driver.wait.until(EC.visibility_of_element_located(locator))
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
        elif field_name == "Hot Foods":
            locator = self.FOOD_HOT_FOOD_LOCATOR
        elif field_name == "Hot Foods":
            locator = self.FOOD_HOT_FOOD_LOCATOR
        elif field_name == "Healthy Choices":
            locator = self.FOOD_HEALTHY_CHOICES_LOCATOR
        elif field_name == "Sandwiches":
            locator = self.FOOD_SANDVICHES_LOCATOR
        elif field_name == "Bakery":
            locator = self.FOOD_BAKERY_LOCATOR
        elif field_name == "Breakfast":
            locator = self.FOOD_BREAKFAST_LOCATOR
        elif field_name == "Pizza":
            locator = self.FOOD_PIZZA_LOCATOR
        elif field_name == "Snacks":
            locator = self.FOOD_SNACKS_LOCATOR
        elif field_name == "Ice Cream":
            locator = self.FOOD_ICE_CREAM_LOCATOR
        elif field_name == "Candy":
            locator = self.FOOD_CANDY_LOCATOR
        elif field_name == "Coffee":
            locator = self.BEVERAGES_COFFEE
        elif field_name == "Cold Pressed Juices":
            locator = self.BEVERAGES_COLD_PRESSED_JUCIES
        elif field_name == "Beer And Wine":
            locator = self.BEVERAGES_BEER_AND_WINE
        elif field_name == "Energy Shots And Drinks":
            locator = self.BEVERAGES_ENERGY_SHOTS_AND_DRINKS
        elif field_name == "Big Gulp":
            locator = self.BEVERAGES_BIG_GULP
        elif field_name == "Slurpee":
            locator = self.BEVERAGES_SLURPEE
        elif field_name == "Get Stimulus Ready":
            locator = self.MONEY_GET_STIMULUS_READY_LOCATOR
        elif field_name == "Financial Services":
            locator = self.MONEY_FINANCIAL_SERVICES_LOCATOR
        elif field_name == "Gift Cards":
            locator = self.MONEY_GIFT_CARDS_LOCATOR
        else:
            raise Exception("No such field name found")
        self.driver.wait.until(EC.element_to_be_clickable(locator)).click()

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
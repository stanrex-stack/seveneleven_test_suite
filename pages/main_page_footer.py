from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPageFooter(Page):
    FACEBOOK_HYPERLINK_LOCATOR = (By.CSS_SELECTOR, '.facebook')
    TWITTER_HYPERLINK_LOCATOR = (By.CSS_SELECTOR, '.twitter')
    INSTAGRAM_HYPERLINK_LOCATOR = (By.CSS_SELECTOR, 'instagram')
    SNAPCHAT_HYPERLINK_LOCATOR = (By.CSS_SELECTOR, '.snapchat')


    SEE_US_LOCATIONS_LOCATOR = (By.CSS_SELECTOR, '.see-us-locations')
    FIND_US_INPUT_LOCATOR = (By.CSS_SELECTOR, 'input#footer-find-us')
    FIND_US_TEXT_LOCATOR = (By.CSS_SELECTOR, '.block-5 h2')

    GET_TO_KNOW_US_TEXT_LOCATOR = (By.CSS_SELECTOR, '.block-0 h2')
    ABOUT_711 = (By.CSS_SELECTOR, '.block-0 a[href*="/about"]')
    BLOG_LOCATOR = (By.CSS_SELECTOR, '.block-0 a[href*="/blog"]')
    CAREERS_LOCATOR = (By.CSS_SELECTOR, '.block-0 a[href*="/careers"]')
    NEWSROOM_LOCATOR = (By.CSS_SELECTOR, '.block-0 a[href*="/newsroom"]')

    FRANCHISE_INFO_TEXT_LOCATOR = (By.CSS_SELECTOR, '.block-1 h2')
    OUR_BUISNESS_MODEL = (By.CSS_SELECTOR, '.block-1 a[href*="/our-business-model"]')
    FRANCHISE_PROCESS = (By.CSS_SELECTOR, '.block-1 a[href*="/new-franchisee"]')
    FRANCHISING_FOR_VETERANS = (By.CSS_SELECTOR, '.block-1 a[href*="/franchises-for-veterans-program"]')

    HOW_WE_CAN_HELP_TEXT_LOCATOR = (By.CSS_SELECTOR, '.block-2 h2')
    CONTACT_US_LOCATOR = (By.CSS_SELECTOR, '.block-2 a[href*="711"]')
    NEW_VENDOR_LOCATION_LOCATOR = (By.CSS_SELECTOR, '.block-2 a[href*="business"]')

    DOWNLOAD_TEXT_LOCATOR = (By.CSS_SELECTOR, '.block-3 h2')
    SEVEN_ELEVEN_APP = (By.CSS_SELECTOR, '.block-3 a[href*="/app"]')
    SEVEN_NOW_DELIVERY_APP = (By.CSS_SELECTOR, '.block-3 a[href*="/7now-app"]')

    TERMS_AND_CONDITIONS = (By.CSS_SELECTOR, '.block-6 a[href*="/terms"]')
    PRIVACY_POLICY = (By.CSS_SELECTOR, '.block-6 a[href*="/privacy"]')

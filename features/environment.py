from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


from python_selenium_automation.ultm_pckg.linda_florida.app.application import Application

def browser_init(context):
    """
    :param context: Behave context
    """
    # context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.driver = webdriver.Firefox()
    context.driver = webdriver.Edge()


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)
    context.driver.wait = WebDriverWait(context.driver, 15)

#   HEADLESS
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless')


#   INCOGNITO
#   options.add_argument("--incognito")

#     EventFiringWebDriver
#     context.driver = EventFiringWebDriver(webdriver.Chrome(), myListner())


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

from selenium.webdriver.common.by import By
from behave import given, when, then

LOCATOR = (By.ID, 'menu-item-0')

@given('Open Main Page')
def open_main_page(context):
    context.app.main_page.open_page()
    context.app.main_page.click(*LOCATOR)

@then("Verify {field} Text is {field_text}")
def verify_field_text(context, field, field_text):
    context.app.main_page_header.verify_field_text(field, field_text)

@then("Verify {item} Is Clickable")
def verify_clickability(context, item):
    context.app.main_page_header.verify_item_is_clickable(item)

@when("Hover Over {field} Button")
def hover_over_header(context, field):
    context.app.main_page_header.hover_over_header_button(field)



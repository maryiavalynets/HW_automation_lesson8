from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


PRODUCT_NAME = (By.CSS_SELECTOR, "span[id ='productTitle']")
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')


@when('Store product name')
def get_product_name(context):
    context.driver.wait.until(EC.element_to_be_clickable(PRODUCT_NAME))
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text


@when('Click on the quantity icon')
def select_quantity(context):
    context.driver.find_element(By.ID, 'a-autoid-0-announce').click()


@when('Choose the 2')
def select_quantity(context):
    context.driver.find_element(By.ID, 'quantity_1').click()


@when('Click on the "Add to Cart" button')
def select_quantity(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@when('Click on the "Cart" button')
def click_on_add_to_cart(context):
    cart_button = context.driver.find_element(By.ID, 'attach-view-cart-button-form')
    cart_button.click()


@when('Hover over New Arrivals option')
def hover_new_arrivals(context):
    context.app.main_page.hover_new_arrivals()


@then('Verify New Arrivals present')
def verify_new_arrivals_present(context):
    context.app.main_page.verify_new_arrivals_present()


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    context.driver.wait.until(EC.visibility_of_all_elements_located(COLOR_OPTIONS))
    expected_colors = ['Black', 'Blue, Over Dye', 'Dark Blue Vintage']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected colors {expected_colors} did not match actual {actual_colors}.'

from selenium.webdriver.common.by import By
from behave import given, when, then


HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')


@given('Open amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()



@when('Click on Returns and Orders button')
def click_on_returns_orders(context):
    #context.driver.find_element(By.ID,'nav-orders').click()
    context.app.main_page.click_order_btn()


@when('Click on the cart icon')
def click_on_cart_icon(context):
    #context.driver.find_element(By.ID,'nav-cart').click()
    context.app.main_page.click_cart_icon()


@when('Input {product} into Amazon search field')
def input_product(context,product):
    element = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    element.clear()
    element.send_keys(product)


@when('Click on the search icon')
def click_on_search_icon(context):
    context.driver.find_element(By.ID,'nav-search-submit-button').click()


@when('Click on the "Best Sellers" link')
def click_on_bestsellers(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id = 'nav_cs_bestsellers']").click()


@when('Search for {product}')
def search_product(context, product):
    #element = context.driver.find_element(*SEARCH_INPUT)
    #element.clear()
    #element.send_keys(product)
    #context.driver.find_element(By.ID, 'nav-search-submit-button').click()
    context.app.main_page.search_product(product)


@when('Select department by value {}')
def select_department(context,select_value):
    context.app.main_page.select_department(select_value)


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    context.driver.find_element(*HAM_MENU)


@then('Verify that footer has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)
    link = context.driver.find_elements(*FOOTER_LINKS)

    assert len(link) == expected_link_count, f'Expected {expected_link_count} links, but got {len(link)}'


@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.search_results_page.verify_department(department)

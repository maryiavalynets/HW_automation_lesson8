from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class MainPage(Page):
    ORDER_BTN = (By.ID,'nav-orders')
    CART_ICON = (By.ID,'nav-cart')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    NEW_ARRIVALS = (By.CSS_SELECTOR, ".nav-a.nav-hasArrow[aria-label='New Arrivals']")
    DEALS = (By.ID, 'nav-flyout-aj:https://m.media-amazon.com/images/G/01/Softlines/Store/MegaMenu/megamenucreator_basic_en_US.json:subnav-sl-megamenu-8:0')

    def open_main(self):
        self.driver.get('https://www.amazon.com/')

    def click_order_btn(self):
        self.driver.find_element(*self.ORDER_BTN).click()

    def click_cart_icon(self):
        self.driver.find_element(*self.CART_ICON).click()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def select_department(self, selection_value):
        select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f'search-alias={selection_value}')

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_new_arrivals_present(self):
        self.wait_for_element_appear(*self.DEALS)


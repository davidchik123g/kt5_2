from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage


class CartPage(BasePage):
    ADD_TO_CART_BTN = (By.XPATH, "//button[@id='button-cart']")
    CART_BUTTON = (By.XPATH, "//a[@title='Shopping Cart']")
    CART_ITEMS = (By.CSS_SELECTOR, "div.container:nth-child(2) div.row div.col div.table-responsive table.table.table-bordered tbody:nth-child(2) tr:nth-child(1) td.text-start.text-wrap:nth-child(2) > a:nth-child(1)")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    CART_CONTENT = (By.CSS_SELECTOR, "#content")

    def add_to_cart(self):
        macbook = self.driver.find_element(By.XPATH, "//a[contains(text(), 'MacBook')]")
        macbook.click()
        add_to_cart_btn = self.find_element(self.ADD_TO_CART_BTN)
        add_to_cart_btn.click()

    def open_cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SUCCESS_ALERT))
        WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(self.SUCCESS_ALERT))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CART_BUTTON))
        cart_button = self.find_element(self.CART_BUTTON)
        cart_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CART_CONTENT))

    def get_cart_items(self):
        return self.find_elements(self.CART_ITEMS)
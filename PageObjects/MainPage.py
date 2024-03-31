import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from BasePage import BasePage


class MainPage(BasePage):
    def open_category(self, category_name):
        category_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(text(),'{category_name}')]"))
        )
        category_link.click()

    def open_category_camera(self):
        category_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Canon EOS 5D')]]"))
        )
        category_link.click()

    def search(self, search_query):
        search_input = self.find_element((By.XPATH,
                                          "//header/div[1]/div[1]/div[2]/div[1]/input[1]"))
        search_input.clear()
        delay = 0.2
        for char in search_query:
            search_input.send_keys(char)
            time.sleep(delay)
        search_button = self.find_element(
            (By.XPATH, "//header/div[1]/div[1]/div[2]/div[1]/button[1]"))
        search_button.click()
        self.driver.implicitly_wait(2)

    PC_CATALOG_LINK = (By.CSS_SELECTOR,
                       "main:nth-child(4) div.container:nth-child(1) nav.navbar.navbar-expand-lg.navbar-light.bg-primary button.navbar-toggler > i.fa-solid.fa-bars")
    PC_CATEGORY_LINK = (By.CSS_SELECTOR,
                        "div.container:nth-child(1) nav.navbar.navbar-expand-lg.navbar-light.bg-primary div.navbar-collapse.collapse.show ul.nav.navbar-nav li.nav-item.dropdown:nth-child(1) > a.nav-link.dropdown-toggle")
    PC_CATEGORY_ITEM = (By.CSS_SELECTOR,
                        "div.container:nth-child(1) nav.navbar.navbar-expand-lg.navbar-light.bg-primary div.navbar-collapse.collapse.show ul.nav.navbar-nav li.nav-item.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a.nav-link")
    PRODUCT_ITEMS = (By.CSS_SELECTOR,
                     "#product-list")

    def open_pc_category(self):
        pc_catalog_link = self.find_element(self.PC_CATALOG_LINK)
        pc_catalog_link.click()
        pc_category_link = self.find_element(self.PC_CATEGORY_LINK)
        pc_category_link.click()
        pc_category_item = self.find_element(self.PC_CATEGORY_ITEM)
        pc_category_item.click()

    def get_product_items(self):
        wait1 = WebDriverWait(self.driver, 10)
        return wait1.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-thumb")))

    def get_pc_items(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#content")))
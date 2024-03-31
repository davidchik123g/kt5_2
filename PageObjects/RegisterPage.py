import time

from selenium.webdriver.common.by import By
from BasePage import BasePage


class RegisterPage(BasePage):
    MY_ACCOUNT_DROPDOWN = (By.XPATH, "//body/nav[@id='top']/div[1]/div[2]/ul[1]/li[2]/div[1]/a[1]")
    REGISTER_LINK = (By.CSS_SELECTOR, "div.container div.nav.float-end:nth-child(2) ul.list-inline li.list-inline-item:nth-child(2) div.dropdown ul.dropdown-menu.dropdown-menu-right.show li:nth-child(1) > a.dropdown-item")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#input-firstname")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    PRIVACY_POLICY_CHECKBOX = (By.CSS_SELECTOR, "div.container:nth-child(2) div.row div.col form:nth-child(3) div.text-end:nth-child(4) div.form-check.form-switch.form-switch-lg.form-check-reverse.form-check-inline > input.form-check-input")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "div.container:nth-child(2) div.row div.col form:nth-child(3) div.text-end:nth-child(4) > button.btn.btn-primary")

    def open_register_page(self):
        my_account_dropdown = self.find_element(self.MY_ACCOUNT_DROPDOWN)
        my_account_dropdown.click()
        register_link = self.find_element(self.REGISTER_LINK)
        register_link.click()

    def register_user(self, first_name, last_name, email, password):
        first_name_input = self.find_element(self.FIRST_NAME_INPUT)
        first_name_input.send_keys(first_name)
        self.driver.implicitly_wait(0.5)
        last_name_input = self.find_element(self.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)
        self.driver.implicitly_wait(0.5)
        email_input = self.find_element(self.EMAIL_INPUT)
        email_input.send_keys(email)
        self.driver.implicitly_wait(0.5)
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.send_keys(password)
        self.driver.implicitly_wait(0.5)
        privacy_policy_checkbox = self.find_element(self.PRIVACY_POLICY_CHECKBOX)
        privacy_policy_checkbox.click()
        self.driver.implicitly_wait(0.5)
        continue_button = self.find_element(self.CONTINUE_BUTTON)
        continue_button.click()
        self.driver.implicitly_wait(0.5)
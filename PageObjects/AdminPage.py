import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage import BasePage
from selenium.webdriver.common.alert import Alert


class AdminPage(BasePage):
    LOGIN_USERNAME_INPUT = (By.ID, "input-username")
    LOGIN_PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    CATALOG_MENU = (By.XPATH, "//header/div[1]/button[1]/i[1]")
    CATALOG_LINK = (
        By.XPATH, "//body/div[@id='container']/nav[@id='column-left']/ul[@id='menu']/li[@id='menu-catalog']/a[1]")
    CATEGORIES_LINK = (By.XPATH, "//a[contains(text(),'Categories')]")
    ADD_NEW_CATEGORY_BUTTON = (
        By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/a[1]/i[1]")
    CATEGORY_NAME_INPUT = (By.CSS_SELECTOR, "#input-name-1")
    CATEGORY_META_TAG_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    CATEGORY_SEO = (
        By.XPATH, "//body/div[@id='container']/div[@id='content']/div[2]/div[1]/div[2]/form[1]/ul[1]/li[3]/a[1]")
    CATEGORY_KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")
    CATEGORY_SAVE_BUTTON = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/button[1]")
    PRODUCT_LINK = (By.XPATH, "//a[normalize-space()='Products']")
    ADD_NEW_PRODUCT_BUTTON = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/a[1]")
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, "#input-name-1")
    PRODUCT_META_TAG_INPUT = (By.CSS_SELECTOR, "#input-meta-title-1")
    PRODUCT_DATA = (By.XPATH, "//a[contains(text(),'Data')]")
    PRODUCT_MODEL_INPUT = (By.XPATH, "//input[@id='input-model']")
    PRODUCT_LINK_LINK = (By.XPATH, "//a[contains(text(),'Links')]")
    PRODUCT_CATEGORIES = (By.CSS_SELECTOR, "#input-category")
    PRODUCT_CATEGORIES_SELECT = (By.XPATH, "//a[contains(text(),'Devices')]")
    CATEGORY_SEO_DEVICES = (By.LINK_TEXT, "SEO")
    CATEGORY_KEYWORD_DEVICES = (By.CSS_SELECTOR, "#input-keyword-0-1")
    PRODUCT_SAVE_BUTTON = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/button[1]")
    DELETE_CHECKBOX_MOUSE = (By.XPATH, "//tbody/tr[3]/td[1]/input[1]")
    PRODUCT_NAME = (By.LINK_TEXT, "Product Name")
    DELETE_CHECKBOX_KEYBOARD = (By.CSS_SELECTOR, "div.container-fluid div.row div.col.col-lg-9.col-md-12 div.card div.card-body div.table-responsive table.table.table-bordered.table-hover tbody:nth-child(2) tr:nth-child(10) td.text-center:nth-child(1) > input.form-check-input")
    DELETE_BUTTON = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/button[3]")
    ALERT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ALERT_MESSAGE = (By.CSS_SELECTOR, "#alert")

    def __init__(self, driver, logger):
        super().__init__(driver, logger)
        self.base_url = "http://localhost/administration/"

    def login(self, username, password):
        self.go_to_site()
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_USERNAME_INPUT))
        username_input.send_keys(username)
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LOGIN_PASSWORD_INPUT))
        password_input.send_keys(password)
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    def create_category(self, category_name, category_meta_tag, category_keyword):
        catalog_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CATALOG_MENU))
        catalog_menu.click()
        catalog_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CATALOG_LINK))
        self.driver.execute_script("arguments[0].click();", catalog_link)
        categories_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CATEGORIES_LINK))
        categories_link.click()
        add_new_category_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_NEW_CATEGORY_BUTTON))
        add_new_category_button.click()
        category_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CATEGORY_NAME_INPUT))
        category_name_input.send_keys(category_name)



        category_meta_tag_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CATEGORY_META_TAG_INPUT))
        category_meta_tag_input.send_keys(category_meta_tag)
        category_seo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CATEGORY_SEO))
        category_seo.click()
        category_keyword_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CATEGORY_KEYWORD))
        category_keyword_input.send_keys(category_keyword)
        category_save_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CATEGORY_SAVE_BUTTON))
        category_save_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ALERT_SUCCESS_MESSAGE))

    def create_product(self, product_name, product_meta_tag, product_model, product_category, product_keyword):
        catalog_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CATALOG_MENU))
        catalog_menu.click()
        product_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PRODUCT_LINK))
        product_link.click()
        add_new_product_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ADD_NEW_PRODUCT_BUTTON))
        add_new_product_button.click()
        product_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_NAME_INPUT))
        product_name_input.send_keys(product_name)
        product_meta_tag_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_META_TAG_INPUT))
        product_meta_tag_input.send_keys(product_meta_tag)
        product_data = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PRODUCT_DATA))
        product_data.click()
        product_model_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_MODEL_INPUT))
        product_model_input.send_keys(product_model)
        product_link_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PRODUCT_LINK_LINK))
        product_link_link.click()
        product_categories = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_CATEGORIES))
        product_categories.send_keys(product_category)
        product_categories_select = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PRODUCT_CATEGORIES_SELECT))
        product_categories_select.click()
        category_seo_devices = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CATEGORY_SEO_DEVICES))
        category_seo_devices.click()
        category_keyword_devices = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CATEGORY_KEYWORD_DEVICES))
        category_keyword_devices.send_keys(product_keyword)
        product_save_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PRODUCT_SAVE_BUTTON))
        product_save_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ALERT_SUCCESS_MESSAGE))

    def delete_product(self):
        catalog_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CATALOG_MENU))
        catalog_menu.click()
        catalog_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.CATALOG_LINK))
        self.driver.execute_script("arguments[0].click();", catalog_link)
        product_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PRODUCT_LINK))
        product_link.click()

        delete_checkbox_mouse = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DELETE_CHECKBOX_MOUSE))
        self.driver.execute_script("arguments[0].click();", delete_checkbox_mouse)

        delete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.DELETE_BUTTON))
        delete_button.click()
        alert = self.driver.switch_to.alert
        alert.accept()

        self.driver.refresh()

        product_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PRODUCT_NAME))
        product_name.click()

        self.driver.execute_script("arguments[0].click();", product_name)
        #без этой команды тест будет ошибку выдавать, я пытался делать без него, но я устал уже пытаться решить данный тест без time.sleep.
        time.sleep(0.5)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        delete_checkbox_keyboard = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DELETE_CHECKBOX_KEYBOARD))
        self.driver.execute_script("arguments[0].click();", delete_checkbox_keyboard)

        actions = ActionChains(self.driver)
        actions.move_to_element(delete_checkbox_keyboard).click().perform()
        #без этой команды тест будет ошибку выдавать, я пытался делать без него, но я устал уже пытаться решить данный тест без time.sleep.
        time.sleep(0.5)



        delete_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.DELETE_BUTTON))
        self.driver.execute_script("arguments[0].click();", delete_button)
        alert = self.driver.switch_to.alert
        alert.accept()

    def go_to_admin_page(self):
        self.driver.get(self.base_url)

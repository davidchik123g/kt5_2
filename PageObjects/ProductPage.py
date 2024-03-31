import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from BasePage import BasePage



class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.container:nth-child(2) div.row div.col div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4:nth-child(4) div.col.mb-3:nth-child(1) div.product-thumb div.content div.description:nth-child(1) h4:nth-child(1) > a:nth-child(1)")
    THUMBNAILS = (By.CSS_SELECTOR, "div.container:nth-child(2) div.row div.col div.row.mb-3 div.col-sm:nth-child(1) div.image.magnific-popup a:nth-child(1) > img.img-thumbnail.mb-3")
    LIGHTBOX_NEXT = (By.CSS_SELECTOR, "body.mfp-zoom-out-cur:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")

    def open_product(self):
        product_name = self.find_element(self.PRODUCT_NAME)
        product_name.click()

    def open_thumbnail(self):
        thumbnail = self.find_elements(self.THUMBNAILS)[0]
        thumbnail.click()

    def next_lightbox(self):
        next_button = self.find_element(self.LIGHTBOX_NEXT)
        next_button.click()

    def add_to_cart(self, product_number):
        add_to_cart_button = self.find_element((By.CSS_SELECTOR,
                                                f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child("
                                                f"4) "
                                                f"div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child("
                                                f"{product_number}) div.product-thumb.transition div.button-group > "
                                                f"button:nth-child(1)"))
        add_to_cart_button.click()

    def add_to_cart_tablet(self):
        add_to_cart_button = self.find_element((By.XPATH,
                                                "//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/button[1]/i[1]"))
        add_to_cart_button.click()

    def add_to_cart_htc(self):
        add_to_cart_button = self.find_element((By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/button[1]"))
        add_to_cart_button.click()

    def add_to_cart_camera(self):
        add_to_cart_button = self.find_element((By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/div[1]/button[1]/i[1]"))
        add_to_cart_button.click()

    def add_to_wishlist(self, product_number):
        add_to_wishlist_button = self.find_element((By.CSS_SELECTOR,
                                                    f"div.container:nth-child(2) div.row div.col div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4:nth-child(4) div.col.mb-3:nth-child(2) div.product-thumb div.content form:nth-child(2) div.button-group:nth-child(1) button:nth-child(2) > i.fa-solid.fa-heart"))
        actions = ActionChains(self.driver)
        actions.move_to_element(add_to_wishlist_button).click().perform()

    def open_product_images(self, product_number):
        product_link = self.find_element((By.CSS_SELECTOR,
                                          f"div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child({product_number}) div.product-thumb.transition div.caption h4:nth-child(1) > a:nth-child(1)"))
        product_link.click()
        product_image = self.find_element((By.CSS_SELECTOR, "div.col-sm-8 ul.thumbnails li:nth-child(1) > a.thumbnail"))
        product_image.click()

    def switch_product_images(self):
        next_image_button = self.find_element((By.CSS_SELECTOR,
                                               "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)"))
        next_image_button.click()

    def open_review_form(self):
        apple_cinema30 = self.find_element((By.XPATH, "//a[contains(text(),'Apple Cinema 30')]"))
        apple_cinema30.click()
        review_link = self.find_element((By.XPATH, "//a[contains(text(),'Reviews (0)')]"))
        self.driver.execute_script("arguments[0].click();", review_link)

    def submit_review(self, name, review_text):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'input-name')))
        name_input.send_keys(name)
        self.driver.implicitly_wait(3)

        review_input = self.find_element((By.ID, 'input-text'))
        review_input.send_keys(review_text)
        self.driver.implicitly_wait(3)

        rating_input = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//body/main[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/form[1]/div[4]/div[1]/input[5]")))

        actions = ActionChains(self.driver)
        actions.move_to_element(rating_input).click().perform()

        self.driver.execute_script("arguments[0].scrollIntoView(true);", rating_input)
        self.driver.implicitly_wait(3)

        rating_input.click()
        self.driver.implicitly_wait(3)

        submit_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#button-review")))
        self.driver.execute_script("arguments[0].click();", submit_button)

        self.driver.implicitly_wait(3)

    def camera(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          "//body/main[1]/div[1]/nav[1]/button[1]/i[1]")))
        camera_option = self.find_element((By.XPATH, "//body/main[1]/div[1]/nav[1]/button[1]/i[1]"))
        camera_option.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "//body/main[1]/div[1]/nav[1]/div[2]/ul[1]/li[7]/a[1]")))
        camera_button = self.find_element((By.XPATH, "//body/main[1]/div[1]/nav[1]/div[2]/ul[1]/li[7]/a[1]"))
        camera_button.click()

    def tablet(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          "//body/main[1]/div[1]/nav[1]/button[1]/i[1]")))
        camera_option = self.find_element((By.XPATH, "//body/main[1]/div[1]/nav[1]/button[1]/i[1]"))
        camera_option.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "//body/main[1]/div[1]/nav[1]/div[2]/ul[1]/li[4]/a[1]")))
        camera_button = self.find_element((By.XPATH, "//body/main[1]/div[1]/nav[1]/div[2]/ul[1]/li[4]/a[1]"))
        camera_button.click()

    def htc(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                          "//body/main[1]/div[1]/nav[1]/button[1]/i[1]")))
        camera_option = self.find_element((By.XPATH, "//body/main[1]/div[1]/nav[1]/button[1]/i[1]"))
        camera_option.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "//body/main[1]/div[1]/nav[1]/div[2]/ul[1]/li[6]/a[1]")))
        camera_button = self.find_element((By.XPATH, "//body/main[1]/div[1]/nav[1]/div[2]/ul[1]/li[6]/a[1]"))
        camera_button.click()
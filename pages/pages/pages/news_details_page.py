from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class NewsDetailsPage(BasePage):

    TITLE = (By.CSS_SELECTOR, "h1")
    CONTENT = (By.CSS_SELECTOR, "app-news-single-page")

    def wait_for_page_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.TITLE))

    def is_title_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).is_displayed()

    def is_content_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.CONTENT)).is_displayed()

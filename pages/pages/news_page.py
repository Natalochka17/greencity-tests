from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class NewsPage(BasePage):

    NEWS_CARDS = (By.CSS_SELECTOR, "app-news-list app-news-list-item")

    FIRST_NEWS = (By.CSS_SELECTOR, "app-news-list app-news-list-item:first-child")

    def wait_for_page_loaded(self):
        return self.wait.until(EC.visibility_of_element_located(self.NEWS_CARDS))

    def get_news_cards(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.NEWS_CARDS))

    def is_news_list_displayed(self):
        cards = self.get_news_cards()
        return len(cards) > 0

    def open_first_news(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NEWS)).click()

import unittest
from selenium import webdriver

from pages.news_page import NewsPage
from pages.news_details_page import NewsDetailsPage


class TestNews(unittest.TestCase):

    URL = "https://www.greencity.cx.ua/#/greenCity/news"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_open_news_page(self):
        news_page = NewsPage(self.driver)

        news_page.open(self.URL)

        news_page.wait_for_page_loaded()

        self.assertTrue(
            news_page.is_news_list_displayed(),
            "News cards are not displayed"
        )

    def test_open_news_details(self):
        news_page = NewsPage(self.driver)

        news_page.open(self.URL)
        news_page.wait_for_page_loaded()

        news_page.open_first_news()

        details_page = NewsDetailsPage(self.driver)

        self.assertTrue(
            details_page.is_title_displayed(),
            "Title is not displayed"
        )
      
        self.assertTrue(
            details_page.is_content_displayed(),
            "Content is not displayed"
        )

    def test_back_to_news(self):
        news_page = NewsPage(self.driver)

        news_page.open(self.URL)
        news_page.wait_for_page_loaded()

        news_page.open_first_news()

        self.driver.back()

        self.assertTrue(
            news_page.is_news_list_displayed(),
            "News list is not displayed after going back"
        )


if __name__ == "__main__":
    unittest.main()

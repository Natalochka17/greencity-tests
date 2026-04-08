import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

class TestGreenCityEvents(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        title = self.driver.title
        self.assertIn("GreenCity", title)

    def test_news_cards_exist(self):
        news_cards = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//app-events-list-item"))
        )
        self.assertGreater(len(news_cards), 0, "Картки новин відсутні")

    def test_first_news_text(self):
        first_news_text = self.wait.until(EC.presence_of_element_located((By.XPATH, "(//app-events-list-item//p)[1]")))
        self.assertTrue(len(first_news_text.text) > 0, "Текст першої новини пустий")

if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

class TestGreenCityEventDetails(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_open_first_news_detail(self):
        first_news = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main/div"))
        )
        first_news.click()

        news_title = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-main/div/div[2]/app-greencity-main/app-events/div/app-events-list/div/div/div[4]/mat-card[2]/app-events-list-item/div/div[3]/div[1]/div[4]/p"))
        )
        self.assertTrue(len(news_title.text) > 0, "Заголовок новини відсутній")

        news_text = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'news-text') or contains(@class,'content')]"))
        )
        self.assertTrue(len(news_text.text) > 0, "Текст новини відсутній")

if __name__ == "__main__":
    unittest.main()

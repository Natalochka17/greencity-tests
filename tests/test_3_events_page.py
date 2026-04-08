import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

class TestGreenCityBackButton(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        self.driver.quit()

    def test_back_button_returns_to_news_list(self):
        first_news = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-main/div/div[2]/app-greencity-main/app-events/div/app-events-list/div/div/div[4]/mat-card[1]/app-events-list-item/div/div[3]/div[1]/div[4]"))
        )
        first_news.click()

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-main/div/div[2]/app-greencity-main/app-events/div/app-events-list/div/div/div[4]/mat-card[1]/app-events-list-item/div/div[3]/div[1]/div[4]"))
        )

        self.driver.back()

        time.sleep(2)

        news_list_container = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-main/div/app-header/header/div[2]/div/div/nav/ul/li[2]"))
        )
        news_cards = news_list_container.find_elements(By.XPATH, "/html/body/app-root/app-main/div/div[2]/app-greencity-main/app-events/div/app-events-list/div/div/div[4]/mat-card[2]/app-events-list-item/div")
        self.assertGreater(len(news_cards), 0, "Список новин не відображається після повернення")

if __name__ == "__main__":
    unittest.main()

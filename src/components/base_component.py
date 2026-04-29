from selenium.webdriver.support.ui import WebDriverWait


class BaseComponent:

    def __init__(self, driver, root):
        self.driver = driver
        self.root = root
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.root.find_element(*locator)

    def click(self, locator):
        self.root.find_element(*locator).click()

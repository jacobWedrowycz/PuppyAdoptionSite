from selenium.webdriver.common.by import By


class PuppyListPage:
    def __init__(self, driver):
        self.driver = driver

    def click_button_by_css_selector(self, css_selector):
        button = self.driver.find_elements(By.CSS_SELECTOR, css_selector)[0]
        button.click()

    def click_next_button(self, css_selector):
        button = self.driver.find_elements(By.CSS_SELECTOR, css_selector)[0]
        button.click()

from selenium.webdriver.common.by import By


class PuppyDetails:
    def __init__(self, driver):
        self.driver = driver

    def click_adopt_me_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "form.button_to[action^='/adoptions'] input.rounded_button")
        button.click()


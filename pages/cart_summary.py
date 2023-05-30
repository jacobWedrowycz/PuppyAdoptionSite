from selenium.webdriver.common.by import By


class CartSummary:
    def __init__(self, driver):
        self.driver = driver

    def select_collar_checkbox(self):
        checkbox = self.driver.find_element(By.XPATH, "//input[@name='collar']")
        checkbox.click()

    def select_toy_checkbox(self):
        checkbox = self.driver.find_element(By.XPATH, "//input[@name='toy']")
        checkbox.click()

    def select_carrier_checkbox(self):
        checkbox = self.driver.find_element(By.XPATH, "//input[@name='carrier']")
        checkbox.click()

    def select_vet_checkbox(self):
        checkbox = self.driver.find_element(By.XPATH, "//input[@name='vet']")
        checkbox.click()

    def click_complete_the_adoption_button(self):
        button = self.driver.find_element(By.XPATH, "//input[@value='Complete the Adoption']")
        button.click()

    def click_adopt_another_puppy_button(self):
        button = self.driver.find_element(By.XPATH, "//input[@value='Adopt Another Puppy']")
        button.click()

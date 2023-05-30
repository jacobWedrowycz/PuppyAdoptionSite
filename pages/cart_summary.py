from selenium.webdriver.common.by import By
import random

class CartSummary:
    def __init__(self, driver):
        self.driver = driver

    def select_checkbox(self, checkbox_id):
        checkbox = self.driver.find_element(By.CSS_SELECTOR, f"input#{checkbox_id}")
        checkbox.click()

    def select_checkboxes(self, checkbox_ids):
        for checkbox_id in checkbox_ids:
            self.select_checkbox(checkbox_id)

    def random_3_checkboxes(self):
        checkboxes = ["collar", "toy", "carrier", "vet"]
        random_checkboxes = random.sample(checkboxes, 3)
        return random_checkboxes

    def click_complete_the_adoption_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "input.rounded_button[value='Complete the Adoption']")
        button.click()

    def click_adopt_another_puppy_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "input.rounded_button[value='Adopt Another Puppy']")
        button.click()

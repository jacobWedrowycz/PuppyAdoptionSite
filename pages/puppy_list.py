from selenium.webdriver.common.by import By
import random


class PuppyListPage:
    def __init__(self, driver):
        self.driver = driver

    def click_details_button_of_brooke(self):
        button = self.driver.find_element(By.CSS_SELECTOR,"form.button_to[action='/puppies/4']")
        button.click()

    def click_details_button_of_sparky(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "form.button_to[action='/puppies/9']")
        button.click()

    def click_random_button_of_puppy(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "form.button_to")
        random_button = random.choice(buttons)
        random_button.click()

    def click_next_navigation_button(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "a.next_page")
        button.click()




from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class FinalizingAdoption:

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, name):
        field_name = self.driver.find_element(By.XPATH, "//input[@name='order[name]']")
        field_name.send_keys(name)

    def enter_address(self, address):
        field_address = self.driver.find_element(By.ID, "order_address")
        field_address.send_keys(address)

    def enter_email(self, email):
        field_email = self.driver.find_element(By.ID, "order_email")
        field_email.send_keys(email)

    def select_pay_type(self, pay_type):
        field_pay_type = self.driver.find_element(By.ID, "order_pay_type")
        select = Select(field_pay_type)
        select.select_by_value(pay_type)

    def click_place_order(self):
        place_order_button = self.driver.find_element(By.CSS_SELECTOR, "button.submit")
        place_order_button.click()

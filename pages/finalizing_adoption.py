from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class FinalizingAdoption:

    def __init__(self, driver):
        self.driver = driver

    def enter_data(self, name, address, email):
        field_name = self.driver.find_element(By.CSS_SELECTOR, "input#order_name")
        field_name.send_keys(name)
        field_address = self.driver.find_element(By.CSS_SELECTOR, "textarea#order_address")
        field_address.send_keys(address)
        field_email = self.driver.find_element(By.CSS_SELECTOR, "input#order_email")
        field_email.send_keys(email)

    def select_pay_type(self, pay_type):
        field_pay_type = self.driver.find_element(By.ID, "order_pay_type")
        select = Select(field_pay_type)
        select.select_by_value(pay_type)

    def click_place_order(self):
        place_order_button = self.driver.find_element(By.CSS_SELECTOR, "button.submit")
        place_order_button.click()

    def check_notice_text(self):
        notice_element = self.driver.find_element(By.ID, 'notice')
        assert notice_element.text == "Thank you for adopting a puppy!"
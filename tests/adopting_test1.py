# My first test with scenario: Adopt Brooke, add a Chewy Toy and a Travel Carrier, pay with Check

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from pages.puppy_list import PuppyListPage
from pages.puppy_details import PuppyDetails
from pages.cart_summary import CartSummary
from pages.finalizing_adoption import FinalizingAdoption

driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
driver.get("https://spartantest-puppies.herokuapp.com/")
title = driver.title

# print the page title
print(title)

# click on specific Puppy named Brook
puppy_list_page = PuppyListPage(driver)
puppy_list_page.click_button_by_css_selector("form.button_to[action='/puppies/4'] input.rounded_button")
time.sleep(1)

# click on 'Adopt Me!' button
puppy_details_page = PuppyDetails(driver)
puppy_details_page.click_adopt_me_button()
time.sleep(1)

# selecting checkboxes and clicking on 'Complete the adoption' button
adoption_page = CartSummary(driver)
adoption_page.select_toy_checkbox()
adoption_page.select_carrier_checkbox()
adoption_page.click_complete_the_adoption_button()
time.sleep(1)

# entering our data, selecting the payment method, and clicking on "Place Order" button
finalizing_page = FinalizingAdoption(driver)
finalizing_page.enter_name("Adam Salamon")
finalizing_page.enter_address("Stachiewicza 40a/18, 30-328 Kraków")
finalizing_page.enter_email("adam.salamon289@gmail.com")
finalizing_page.select_pay_type("Check")
finalizing_page.click_place_order()
time.sleep(1)



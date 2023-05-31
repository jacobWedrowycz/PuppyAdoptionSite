# My first test with scenario: Adopt Brooke, add a Chewy Toy and a Travel Carrier, pay with Check

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.puppy_list import PuppyListPage
from pages.puppy_details import PuppyDetails
from pages.cart_summary import CartSummary
from pages.finalizing_adoption import FinalizingAdoption

driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
driver.get("https://spartantest-puppies.herokuapp.com/")
title = driver.title

puppy_list_page = PuppyListPage(driver)
puppy_details_page = PuppyDetails(driver)
adoption_page = CartSummary(driver)
finalizing_page = FinalizingAdoption(driver)

# print the page title
print(title)

# click on specific Puppy named Brook
puppy_list_page.click_details_button_of_brooke()

# click on 'Adopt Me!' button
puppy_details_page.click_adopt_me_button()

# select checkboxes and click on 'Complete the adoption' button
checkboxes_to_select = ["collar", "toy"]
adoption_page.select_checkboxes(checkboxes_to_select)
time.sleep(1)
adoption_page.click_complete_the_adoption_button()

# enter our data, select the payment method, and click on "Place Order" button
finalizing_page.enter_data("Adam Salamon", "Stachiewicza 40a/18, 30-328 Kraków", "adam.salamon289@gmail.com")
finalizing_page.select_pay_type("Check")
finalizing_page.click_place_order()
time.sleep(1)

# check if the puppy became successfully adopted
finalizing_page.check_notice_text()
print("Puppy became successfully adopted - test passed")
driver.close()

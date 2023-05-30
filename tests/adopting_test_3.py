# My third test with scenario: Adopt 2 Random Dogs add a Collar & Leash to each, pay with Credit Card

from selenium import webdriver
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


# selecting a first random puppy
puppy_list_page = PuppyListPage(driver)
puppy_list_page.click_random_button_of_puppy()

# click on 'Adopt Me!' button
puppy_details_page = PuppyDetails(driver)
puppy_details_page.click_adopt_me_button()

# selecting collar checkbox and click on 'Adopt Another Puppy' button
adoption_page = CartSummary(driver)
checkboxes_to_select = ["collar"]
adoption_page.select_checkboxes(checkboxes_to_select)
adoption_page.click_adopt_another_puppy_button()

# selecting a second random puppy on second page
puppy_list_page = PuppyListPage(driver)
puppy_list_page.click_next_navigation_button()
puppy_list_page.click_random_button_of_puppy()
puppy_details_page.click_adopt_me_button()

adoption_page = CartSummary(driver)
adoption_page.click_complete_the_adoption_button()

# entering our data, selecting the payment method, and clicking on "Place Order" button
finalizing_page = FinalizingAdoption(driver)
finalizing_page.enter_data("Adam Salamon", "Stachiewicza 40a/18, 30-328 Kraków", "adam.salamon289@gmail.com")
finalizing_page.select_pay_type("Credit card")
finalizing_page.click_place_order()

# checking if the puppy became successfully adopted
finalizing_page.check_notice_text()
print("2 random Puppies became successfully adopted - test passed")
driver.close()


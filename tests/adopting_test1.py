from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(r'C:\TestFiles\chromedriver.exe'))
driver.get("https://spartantest-puppies.herokuapp.com/")
title = driver.title
print(title)
assert 'The Spartan\'s Puppy Adoption Agency' == title

ViewDetailsButton1 = driver.find_element(By.CSS_SELECTOR, "form.button_to[action='/puppies/4'] input.rounded_button")
ViewDetailsButton1.click()

AdoptMeButton1 = driver.find_element(By.CSS_SELECTOR, "form.button_to[action='/adoptions?puppy_id=4'] "
                                                      "input.rounded_button")
AdoptMeButton1.click()

checkbox1 = driver.find_element(By.XPATH, "//input[@name='toy']")
checkbox2 = driver.find_element(By.XPATH, "//input[@name='carrier']")

if not checkbox1.is_selected():
    checkbox1.click()

if not checkbox2.is_selected():
    checkbox2.click()

ViewDetailsButton1 = driver.find_element(By.CSS_SELECTOR, "form.button_to[action='/orders/new'] input.rounded_button")
ViewDetailsButton1.click()

field_name = driver.find_element(By.ID, "order_name")
field_address = driver.find_element(By.ID, "order_address")
field_email = driver.find_element(By.ID, "order_email")
field_pay_type = driver.find_element(By.ID, "order_pay_type")

field_name.send_keys("Adam Salamon")
field_address.send_keys("Stachiewicza 40a/18, 30-328 Kraków")
field_email.send_keys("adam.salamon289@gmail.com")
field_pay_type.click()
option_check = driver.find_element(By.XPATH, "//select[@id='order_pay_type']/option[@value='Check']")
option_check.click()

PlaceOrderButton = driver.find_element(By.CSS_SELECTOR, "button.submit")
PlaceOrderButton.click()

time.sleep(5) #sleep for 5sec before closing browser


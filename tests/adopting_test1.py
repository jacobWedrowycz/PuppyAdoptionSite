from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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




time.sleep(5) #sleep for 5sec before closing browser


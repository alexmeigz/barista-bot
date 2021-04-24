from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

PATH = "C:/Users/hanso/Documents/CS_Projects/Robotics Project/Chrome Driver/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
driver = webdriver.Chrome(PATH, options=chrome_options)


driver.get("https://www.allrecipes.com/recipes/77/drinks/")

time.sleep(3)
# close = driver.find_element_by_xpath('//*[@id="bx-close-inside-1159576"]/svg')
# close.click()
# time.sleep(10)
# close2 = driver.find_element_by_xpath('//*[@id="bx-close-inside-1026268"]/svg')
# close2.click()

load = driver.find_element_by_link_text("LOAD MORE")
for i in range(2):
    load.click()
    time.sleep(1)


recipes = driver.find_elements_by_xpath('/html/body/main/div[8]/div/div[1]/div/div[2]/div/a')
num_recipes = len(recipes)

print(num_recipes)
for i in range(num_recipes):
    recipes = driver.find_elements_by_xpath('/html/body/main/div[8]/div/div[1]/div/div[2]/div/a')
    if len(recipes) < i - 1:
        load.click()
    recipes[i].send_keys(Keys.RETURN)
    print(i)
    driver.back()




time.sleep(20)
driver.quit()


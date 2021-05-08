from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time
import os
import json

PATH = "C:/Users/hanso/Documents/CS_Projects/Robotics Project/Chrome Driver/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
driver = webdriver.Chrome(PATH, options=chrome_options)


# driver.get("https://www.allrecipes.com/recipes/77/drinks/")

# time.sleep(3)
# close = driver.find_element_by_xpath('//*[@id="bx-close-inside-1159576"]/svg')
# close.click()
# time.sleep(10)
# close2 = driver.find_element_by_xpath('//*[@id="bx-close-inside-1026268"]/svg')
# close2.click()

# load = driver.find_element_by_link_text("LOAD MORE")
# for i in range(2):
#     load.click()
#     time.sleep(1)

badLinks = ["https://www.allrecipes.com/article/how-to-make-hot-chocolate/", "https://www.allrecipes.com/recipe/20216/simple-syrup/", "https://www.allrecipes.com/recipe/180917/tom-and-jerry-batter/"]
count = 0
recipeLinks = []
for i in range(2,167):
    driver.get("https://www.allrecipes.com/recipes/77/drinks/?page=" + str(i))
    recipes = driver.find_elements_by_class_name('tout__titleLink')
    for item in recipes:
        link = item.get_attribute('href')
        if not link in badLinks:
            if "/recipe/" in link:
                recipeLinks.append(link)

# for link in recipeLinks:
#     link.click()
#     title = driver.find_element_by_class_name('headline heading-content').get_attribute('innerHTML')
#     print(title)
#     driver.back()

num_recipes = len(recipeLinks)
print(num_recipes)
with open("recipes.json", "w") as fp:   #Pickling
     json.dump(recipeLinks, fp)



driver.quit()

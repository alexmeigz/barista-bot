import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time
from tqdm import tqdm

PATH = "C:/Users/hanso/Documents/CS_Projects/Robotics Project/Chrome Driver/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=3')
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("enable-automation")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_extension('Adblock-Plus_v1.4.1.crx')
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(PATH, options=chrome_options)


jsonFile = open('recipeCleaned.json', 'r')
recipeUrls = []
recipeUrls = json.load(jsonFile)

jsonFile2 = open('recipeList.json', 'r')
recipeList = []
recipeList = json.load(jsonFile2)

recipeLen = len(recipeList)

def readRecipe(link):
    recipe = {}
    driver.get(link)
    time.sleep(5)
    recipe["title"] = driver.find_element_by_tag_name('h1').text
    ingredients = driver.find_elements_by_class_name('ingredients-item-name')
    recipe["ingredients"] = [item.text for item in ingredients]
    directions = driver.find_elements_by_xpath('/html/body/div[2]/div/main/div[1]/div[2]/div[1]/div[2]/div[2]/section[1]/fieldset/ul/li/div/div/p')
    recipe["directions"] = [item.text for item in directions]
    return recipe


for i in tqdm(range(recipeLen, recipeLen + 25)):
    recipeList.append(readRecipe(recipeUrls[i]))

print(recipeLen)

with open("recipeList.json", "w") as fp: 
     json.dump(recipeList, fp)



driver.quit()
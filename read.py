import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time

PATH = "C:/Users/hanso/Documents/CS_Projects/Robotics Project/Chrome Driver/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
driver = webdriver.Chrome(PATH, options=chrome_options)


jsonFile = open('recipes.json', 'r')
recipeList = []
recipeList = json.load(jsonFile)
print(len(recipeList))

def readRecipe(link):
    
import json


jsonFile = open('recipes.json', 'r')
recipeUrls = []
recipeUrls = json.load(jsonFile)

badWords = ["vodka", "cocktail", "rum", "margarita", "whiskey", "martini", "mojito", "sangria", "jager", "tequila", "moonshine", "bellini", "brandy", "agua", "fresca", "gin","julep", "guinness", "beer", "shot", "pina", "colada", "alcohol"]

cleanList = []
for i in range(len(recipeUrls)):
    bad = False
    for badWord in badWords:
        if badWord in recipeUrls[i]:
            bad = True
    if "virgin" in recipeUrls[i]:
        bad = False
    if not bad:
        cleanList.append(recipeUrls[i])

print(len(recipeUrls))
print(len(cleanList))

with open("recipeCleaned.json", "w") as fp: 
     json.dump(cleanList, fp)
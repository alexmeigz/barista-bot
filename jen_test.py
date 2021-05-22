import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# decorator that links the route with the function
@app.route('/', methods=['GET'])
def getRecipe():
    query_parameters = request.args
    print(query_parameters)
    print(type(query_parameters))
    recipe_name = query_parameters.get("recipe_title")
    print(recipe_name)
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/recipes', methods=['POST'])
def postRecipe():
    return "Recipe suggestion"

app.run()
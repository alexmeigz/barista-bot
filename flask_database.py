from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

## user profile- name, sweetness, ice, acidity, size, allergies, vegan, vegetarian, toppings

class User_profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    vegan = db.Column(db.Boolean, unique = False, nullable = False)
    vegetarian = db.Column(db.Boolean, unique = False, nullable = False)
    sweetness = db.Column(db.Integer, unique = False, nullable = False)
    ice = db.Column(db.Integer, unique = False, nullable = False)
    acidity = db.Column(db.Integer, unique = False, nullable = False)
    allergies = db.Column(db.String(800), unique = False, nullable = False)
    toppings = db.Column(db.String(800), unique = False, nullable = False)

class Ingredient_tuple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity =  db.Column(db.Integer, unique=False, nullable=False)
    measurement =  db.Column(db.String(800), unique=False, nullable=True)
    ingredient = db.Column(db.String(800), unique=False, nullable=True)
    recipeName = db.Column(db.String(800), unique=False, nullable=True)

## dict["blueberry smoothie"] = [(2,cups,yogurt),(1, tablespoon,honey), (1, bucket, feet)]
@app.route('/', methods=['POST'])
def postRecipe():
    d = {}
    d["blueberry smoothie"] = [(2,"cups","yogurt"),(1, "tablespoon","honey"),(1, "bucket", "feet")]
    for key in d:
        for l in d[key]:
            ing = Ingredient_tuple(quantity=l[0], measurement=l[1], ingredient=l[2], recipeName=key)
            db.session.add(ing)
    db.session.commit()
    return 'Hello, Flask!'

@app.route('/', methods=['GET'])
def getRecipe():
    query_parameters = request.args
    recipe_name = query_parameters.get("recipe_title")
    print(recipe_name)
    ings = Ingredient_tuple.query.filter_by(recipeName=recipe_name).all()
    print(ings)
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run()

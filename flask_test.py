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

@app.route('/')
def index():
	user = User_profile(name = request.args.get("name", ""), email = request.args.get("email", ""), vegan = request.args.get("vegan", False) == "True", vegetarian = request.args.get("vegetarian", False) == "True", 
	sweetness = int(request.args.get("sweetness", 100)), ice = int(request.args.get("ice", 100)), acidity = int(request.args.get("acidity", 0)), allergies = request.args.get("allergies", ""), 
	toppings = request.args.get("toppings", ""))
	db.session.add(user)
	db.session.commit()
	return 'Hello, Flask!'

if __name__ == '__main__':
	app.run(debug=True)

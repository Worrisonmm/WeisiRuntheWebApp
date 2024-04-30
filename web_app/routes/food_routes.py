from flask import Blueprint, render_template, current_app #, session

from app.models.food import Food

food_routes = Blueprint("food_routes", __name__)

@food_routes.route("/foods")
def foods():
    foods = Food.all()
    return render_template("foods.html", foods=foods)
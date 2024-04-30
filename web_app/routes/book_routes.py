from flask import Blueprint, render_template, current_app #, session

from app.models.food import Foods

foods_routes = Blueprint("foods_routes", __name__)

@foods_routes.route("/foods")
def foods():
    foods = Foods.all()
    return render_template("foods.html", foods=foods)

from app.db import BaseModel

class Food(BaseModel):

    SHEET_NAME = "foods"

    COLUMNS = ["name", "type"]

    SEEDS = [
        {"name": "Chow Mien", "type": "Entree"},
        {"name": "Pudding", "type": "Dessert"},
        {"name": "Steak", "type": "Entree"},
        {"name": "Cheese Cake", "type": "Dessert"},
        {"name": "Pasta", "type": "Entree"},
       
    ]

if __name__ == "__main__":

    foods = Food.all()
    print("FOUND", len(foods), "BOOKS")
    if any(foods):
        for food in foods:
            print(food.title, food.author, food.year)
    else:
        Food.seed()



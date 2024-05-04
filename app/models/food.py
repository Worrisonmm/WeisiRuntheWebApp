from app.db import BaseModel

class Food(BaseModel):

    SHEET_NAME = "foods"

    COLUMNS = ["name", "type"]

    SEEDS = [
        {"name": "Chow Mien", "type": "Entree"},
        {"name": "Sandwich", "type": "Entree"},
        {"name": "Steak", "type": "Entree"},
        {"name": "BAJA Fish Taco", "type": "Entree"},
        {"name": "Whiting Fish Nuggets", "type": "Entree"},
        {"name": "Hot Pot", "type": "Entree"},
        {"name": "Beef Kidney", "type": "Side"},
        {"name": "Hush Puppies", "type": "Side"},
        {"name": "Pudding", "type": "Dessert"},
        {"name": "Cheese Cake", "type": "Dessert"},
        {"name": "Carrot Cake", "type": "Dessert"},
    
       
        

       
    ]

if __name__ == "__main__":

    foods = Food.all()
    print("FOUND", len(foods), "BOOKS")
    if any(foods):
        for food in foods:
            print(food.title, food.author, food.year)
    else:
        Food.seed()



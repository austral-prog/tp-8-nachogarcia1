from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients = set(dish_ingredients)
    a, b = dish_name, dish_ingredients
    return a, b


def check_drinks(drink_name, drink_ingredients):
    set_ingredients = set(drink_ingredients)
    if len(set_ingredients.intersection(ALCOHOLS)) > 0:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


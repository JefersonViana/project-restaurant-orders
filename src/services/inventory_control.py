from csv import DictReader
from typing import Dict

from models.dish import Recipe
from models.ingredient import Ingredient

BASE_INVENTORY = "data/inventory_base_data.csv"

Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BASE_INVENTORY) -> Inventory:
    inventory = dict()

    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])

    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path=BASE_INVENTORY) -> None:
        self.inventory = read_csv_inventory(inventory_file_path)

    def check_recipe_availability(self, recipe: Recipe) -> bool:
        for ing, qtd in recipe.items():
            if ing not in self.inventory or self.inventory[ing] < qtd:
                return False
        return True

    def consume_recipe(self, recipe: Recipe) -> None:
        # if self.check_recipe_availability(recipe):
        dict_ingredients = {}
        for ing, qtd in recipe.items():
            if self.inventory[ing] - qtd < 0:
                raise ValueError
            else:
                dict_ingredients[ing] = qtd
        for one, two in dict_ingredients.items():
            self.inventory[one] -= two
        # else:
        #     raise ValueError()

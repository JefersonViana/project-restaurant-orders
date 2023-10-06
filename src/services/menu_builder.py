from typing import Dict, List, Set

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from models.dish import Dish

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> List[Dict]:
        dishes: Set[Dish] = self.menu_data.dishes
        # print(self.inventory.inventory)
        # for x, y in self.inventory.inventory.items():
        #     if y == 300:
        #         return []
        if restriction:
            return [
                {
                    "dish_name": dish.name,
                    "price": dish.price,
                    "ingredients": dish.get_ingredients(),
                    "restrictions": dish.get_restrictions()
                }
                for dish in dishes
                if restriction not in dish.get_restrictions()
                if self.inventory.check_recipe_availability(
                    dish.get_all_recipes()
                )
            ]
        else:
            return [
                {
                    "dish_name": dish.name,
                    "price": dish.price,
                    "ingredients": dish.get_ingredients(),
                    "restrictions": dish.get_restrictions()
                }
                for dish in dishes
                if self.inventory.check_recipe_availability(
                    dish.get_all_recipes()
                )
            ]


# menu = MenuBuilder(
#         data_path=DATA_PATH,
#         inventory_path="tests/mocks/inventory_base_data_2.csv"
#     ).get_main_menu()
# print(menu)
# IMPLEMENTAÇÃO USANDO UM FOR DE FORMA COMUM!!
# def get_main_menu(self, restriction=None) -> List[Dict]:
#     data = list()
#     dishes: Set[Dish] = self.menu_data.dishes
#     if restriction:
#         for dish in dishes:
#             if restriction not in dish.get_restrictions():
#                 data.append({
#                     "dish_name": dish.name,
#                     "price": dish.price,
#                     "ingredients": dish.get_ingredients(),
#                     "restrictions": dish.get_restrictions()
#                 })
#     else:
#         for dish in dishes:
#             data.append({
#                     "dish_name": dish.name,
#                     "price": dish.price,
#                     "ingredients": dish.get_ingredients(),
#                     "restrictions": dish.get_restrictions()
#                 })
#     return data

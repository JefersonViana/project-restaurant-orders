from models.dish import Dish, Ingredient
import csv
from abc import abstractmethod


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        exist_dish = {}
        for dish in self.read_file(source_path):
            if dish[0] in exist_dish:
                exist_dish[dish[0]].add_ingredient_dependency(
                        Ingredient(dish[2]), int(dish[3])
                    )
            else:
                exist_dish[dish[0]] = Dish(dish[0], float(dish[1]))
                exist_dish[dish[0]].add_ingredient_dependency(
                    Ingredient(dish[2]), int(dish[3])
                )
        for dish in exist_dish.values():
            self.dishes.add(dish)

    @abstractmethod
    def read_file(self, source_path):
        with open(source_path, encoding="utf-8") as file:
            header, *data = csv.reader(file, delimiter=",", quotechar='"')
        return data

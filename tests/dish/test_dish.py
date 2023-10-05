import pytest
from src.models.dish import Dish, Ingredient # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 2
def test_dish():
    dish_1 = Dish("lasanha", 25.00)
    dish_2 = Dish("lasanha", 25.00)
    dish_3 = Dish("pizza", 15.00)
    ingredient = Ingredient("queijo parmesão")
    dish_1.add_ingredient_dependency(ingredient, 5)
    assert dish_1.get_restrictions() == {Restriction.ANIMAL_DERIVED,
                                         Restriction.LACTOSE}
    assert dish_1.__repr__() == "Dish('lasanha', R$25.00)"
    assert dish_1 == dish_2
    assert hash(dish_1) == hash(dish_2)
    assert hash(dish_1) != hash(dish_3)
    assert dish_1.name == "lasanha"
    assert len(dish_1.recipe) == 1
    assert len(dish_1.get_ingredients()) == 1
    assert dish_1.recipe.get(ingredient) == 5
    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish('lasanha', 0)
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('lasanha', "2")

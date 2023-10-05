from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("queijo parmesão")
    ingredient_2 = Ingredient("queijo parmesão")
    ingredient_3 = Ingredient("queijo provolone")
    assert ingredient_1.name == "queijo parmesão"
    assert hash(ingredient_1) == hash(ingredient_2)
    assert hash(ingredient_1) != hash(ingredient_3)
    assert ingredient_1.restrictions == {Restriction.ANIMAL_DERIVED,
                                         Restriction.LACTOSE}
    assert ingredient_1.__repr__() == "Ingredient('queijo parmesão')"
    assert ingredient_1 == ingredient_2

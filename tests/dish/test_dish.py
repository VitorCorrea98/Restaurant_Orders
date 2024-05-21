from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    new_dish = Dish("frango", 25.00)
    new_dish_2 = Dish("frango", 25.00)

    assert new_dish.name == "frango"
    assert new_dish == new_dish_2
    assert hash(new_dish) == hash(new_dish_2)
    assert hash(new_dish) == hash("Dish('frango', R$25.00)")

    with pytest.raises(TypeError):
        Dish("frango", "R25.00")

    with pytest.raises(ValueError):
        Dish("frango", -10)

    new_ingredient = Ingredient("frango")
    new_dish.add_ingredient_dependency(new_ingredient, 300)
    assert new_dish.get_restrictions() == new_ingredient.restrictions
    assert new_dish.get_ingredients() == {new_ingredient}

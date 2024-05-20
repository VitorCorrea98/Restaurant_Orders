from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    new_ingredient = Ingredient("ovo")
    new_ingredient_2 = Ingredient("frango")
    assert hash(new_ingredient) == hash("ovo")
    assert new_ingredient.name == "ovo"

    assert hash(new_ingredient_2) == hash("frango")
    assert new_ingredient_2.name == "frango"

    assert new_ingredient == new_ingredient
    assert new_ingredient != new_ingredient_2
    assert hash(new_ingredient) != hash(new_ingredient_2)

    assert repr(new_ingredient) == "Ingredient('ovo')"
    assert repr(new_ingredient_2) == "Ingredient('frango')"

    assert Restriction.LACTOSE not in new_ingredient.restrictions
    assert Restriction.ANIMAL_DERIVED in new_ingredient.restrictions

    assert Restriction.ANIMAL_DERIVED in new_ingredient_2.restrictions
    assert Restriction.ANIMAL_MEAT in new_ingredient_2.restrictions
